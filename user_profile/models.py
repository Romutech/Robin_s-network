from django.db import models

class Profile(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    date_of_birth = models.DateField(null=True)
    profession = models.CharField(max_length=50, null=True)
    residence = models.CharField(max_length=50, null=True)
