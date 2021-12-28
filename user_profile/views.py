from django.shortcuts import render, redirect
from .forms import UserProfileForm
from .models import UserProfile


def create_or_update_profile(request):
    profile = None
    if UserProfile.is_exist(request):
        profile = request.user.user_profile
    form = UserProfileForm(request.POST or None, instance=profile)
    if form.is_valid():
        user_profile = form.save(commit=False)
        user_profile.user = request.user
        user_profile.save()
        return redirect('read_profile')
    return render(request, 'user_profile/edit_profile.html', locals())


def read_profile(request):
    if not UserProfile.is_exist(request):
        return redirect('edit_profile')
    profile = request.user.user_profile
    return render(request, 'user_profile/profile.html', locals())
