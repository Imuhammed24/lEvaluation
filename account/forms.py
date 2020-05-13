from django import forms
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label='', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField( label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
