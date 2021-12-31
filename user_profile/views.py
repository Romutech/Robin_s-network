from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserProfileForm, ProfilePictureForm
from .models import UserProfile, ProfilePicture


def create_or_update_profile(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    picture_connected_user = ProfilePicture.get_profile_picture_if_exists(
        request.user
    )
    profile = None
    if UserProfile.is_exist(request):
        profile = request.user.user_profile
    form = UserProfileForm(request.POST or None, instance=profile)
    if form.is_valid():
        user_profile = form.save(commit=False)
        user_profile.user = request.user
        user_profile.save()
        return redirect('read_profile', request.user.id)
    return render(request, 'user_profile/edit_profile.html', locals())


def read_profile(request, user_id):
    if request.user.is_authenticated:
        picture_connected_user = ProfilePicture.get_profile_picture_if_exists(
            request.user
        )
        name_connected_user = f"{request.user.user_profile.first_name} " \
                              f"{request.user.user_profile.last_name}"
    try:
        if not user_id.isnumeric():
            return render(request, 'user_profile/404.html', locals())
        profile = UserProfile.objects.get(user_id=user_id)
    except UserProfile.DoesNotExist:
        return render(request, 'user_profile/404.html', locals())
    profile_picture = ProfilePicture.get_profile_picture_if_exists(
        profile.user
    )
    return render(request, 'user_profile/profile.html', locals())


def upload_profile_picture(request):
    if request.user.is_authenticated:
        print("oui loggé")
    else:
        print("non pas loggué")

    picture_connected_user = ProfilePicture.get_profile_picture_if_exists(
        request.user
    )
    profile_picture = None
    profile_picture = ProfilePicture.get_profile_picture_if_exists(
        request.user
    )
    form = ProfilePictureForm(
        request.POST or None, request.FILES or None, instance=profile_picture
    )
    if form.is_valid():
        profile_picture = form.save(commit=False)
        profile_picture.user = request.user
        profile_picture.save()
        return redirect('read_profile', request.user.id)
    return render(
        request, 'user_profile/upload_profile_picture.html', locals()
    )


@login_required
def delete_profile_picture(request):
    profile_picture = ProfilePicture.get_profile_picture_if_exists(
        request.user
    )
    if profile_picture:
        profile_picture.delete()
    return redirect('read_profile', request.user.id)
