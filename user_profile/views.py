from django.shortcuts import render, redirect
from .forms import UserProfileForm, ProfilePictureForm
from .models import UserProfile, ProfilePicture


def create_or_update_profile(request):
    if UserProfile.is_exist(request):
        profile = request.user.user_profile
    if ProfilePicture.is_exist(request):
        profile_picture = request.user.profile_picture
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
    if ProfilePicture.is_exist(request):
        profile_picture = request.user.profile_picture
    profile = request.user.user_profile
    return render(request, 'user_profile/profile.html', locals())


def upload_profile_picture(request):
    profile_picture = None
    if UserProfile.is_exist(request):
        profile = request.user.user_profile
    if ProfilePicture.is_exist(request):
        profile_picture = request.user.profile_picture
    form = ProfilePictureForm(
        request.POST or None, request.FILES or None, instance=profile_picture
    )
    if form.is_valid():
        profile_picture = form.save(commit=False)
        profile_picture.user = request.user
        profile_picture.save()
        return redirect('read_profile')
    return render(
        request, 'user_profile/upload_profile_picture.html', locals()
    )


def delete_profile_picture(request):
    if ProfilePicture.is_exist(request):
        profile_picture = request.user.profile_picture
        profile_picture.delete()
    return redirect('read_profile')
