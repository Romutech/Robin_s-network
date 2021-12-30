from django import forms
from .models import UserProfile, ProfilePicture


class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=True, label="Prénom")
    last_name = forms.CharField(required=False, label="Nom")
    date_of_birth = forms.DateField(
        required=False,
        label="Date de naissance",
        help_text="Veuillez saisir une date au format ‹‹ jour/mois/année ››. "
                  "Exemple : 13/06/1981"
    )
    profession = forms.CharField(required=False, label="Profession")
    residence = forms.CharField(required=False, label="Lieu de résidence")

    class Meta:
        model = UserProfile
        exclude = ['user']


class ProfilePictureForm(forms.ModelForm):
    picture = forms.ImageField(required=True, label="Photo de profil")
    class Meta:
        model = ProfilePicture
        exclude = ['user']
