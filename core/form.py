from django.forms import ModelForm
from . models import UserProfile
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms
from django.utils.translation import gettext, gettext_lazy as _


class LoginForm(AuthenticationForm):
    username = UsernameField(
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True, 'class': 'input100'}),
    )
    password = forms.CharField(label=_("Password"), strip=False,
                               widget=forms.PasswordInput(attrs={'class': 'input100'}))
