from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

import sys
sys.path.append('..')
from locations.models import Area


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(forms.Form):

    locations = []

    first_name = forms.CharField(max_length=100, help_text='First Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    username = forms.CharField(max_length=100, help_text='username')
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(max_length=150, help_text='Email')
    location = forms.ModelChoiceField(queryset=Area.objects.all())
