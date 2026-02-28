from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EditForm(forms.ModelForm):
    class Meta:

        model = Profile
        exclude = ['user']