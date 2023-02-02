from .models import *
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


class UserRegisterationForm(UserCreationForm):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    firstname = forms.CharField(max_length=20)
    lastname =  forms.CharField(max_length=20)
    password = forms.PasswordInput()
    class Meta:
        model = User
        fields = ('username','email','firstname','lastname','password1','password2')
    


# A form to create users profile
class UserUpdateForm(UserChangeForm):
    
    class Meta:
        model = User
        fields = '__all__'


# form to update the profile fields
class UpdateProfileForm(forms.ModelForm):
    model = UserProfile
    fields = ['age','country']
    