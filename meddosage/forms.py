from .models import *
from django import forms


class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        field = "__all__"
        
        