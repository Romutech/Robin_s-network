from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=50, label="Email")
    password = forms.CharField(
        widget=forms.PasswordInput(), label="Mot de passe"
    )


class RegisterForm(forms.Form):
    email = forms.EmailField(max_length=50, label="Email")
    password = forms.CharField(
        widget=forms.PasswordInput(), label="Mot de passe"
    )
