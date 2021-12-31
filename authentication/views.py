from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from authentication.forms import LoginForm


def user_login(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        try:
            user = User.objects.get(email=form.cleaned_data['email'])
        except User.DoesNotExist:
            messages.error(request, 'Identifiant ou mot de passe inconnu !')
            return render(request, 'authentication/user_login.html', locals())
        user = authenticate(
            request,
            username=user.username,
            password=form.cleaned_data['password']
        )
        if user is not None:
            login(request, user)
            return redirect('read_profile', user.id)
        else:
            messages.error(request, 'Identifiant ou mot de passe inconnu !')
    return render(request, 'authentication/user_login.html', locals())


def user_logout(request):
    logout(request)
    return redirect('user_login')
