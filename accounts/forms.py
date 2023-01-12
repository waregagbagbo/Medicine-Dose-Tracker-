from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterationForm(UserCreationForm):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    firstname = forms.CharField(max_length=20)
    lastname =  forms.CharField(max_length=20)
    password = forms.PasswordInput()
    class Meta:
        model = User
        fields = ('username','email','firstname','lastname','password1','password2')
    
