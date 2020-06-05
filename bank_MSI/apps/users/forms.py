# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email', 'nation', 'pob', 'por', 'dob', 'marry', 'name', 'gender', 'img')

class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'nation', 'pob', 'por', 'dob', 'marry', 'name', 'gender', 'img')