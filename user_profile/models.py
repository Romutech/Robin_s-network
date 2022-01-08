from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="user_profile"
    )
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    date_of_birth = models.DateField(null=True)
    profession = models.CharField(max_length=50, null=True)
    residence = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def is_exist(request):
        try:
            request.user.user_profile
            return True
        except UserProfile.DoesNotExist:
            return False


class ProfilePicture(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="profile_picture"
    )
    picture = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_profile_picture(user):
        try:
            profile_picture = user.profile_picture
            return profile_picture
        except ProfilePicture.DoesNotExist:
            return None
