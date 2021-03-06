from locations.models import Area, Location
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

import sys
sys.path.append('..')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(max_length=150)

    location = forms.ModelChoiceField(queryset=Area.objects.all())
