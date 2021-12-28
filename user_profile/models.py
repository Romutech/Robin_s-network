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

    @staticmethod
    def is_exist(request):
        try:
            request.user.user_profile
            return True
        except UserProfile.DoesNotExist:
            return False
