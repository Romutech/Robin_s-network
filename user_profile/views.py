from django.shortcuts import render


def read_profile_view(request):
    profile = request.user.user_profile
    return render(request, 'user_profile/profile.html', locals())
