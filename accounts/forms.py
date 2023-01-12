from .models import *
from django.forms import ModelForm

class UserRegisterationForm(ModelForm):
    
    class Meta:
        fields = '__all__'
        