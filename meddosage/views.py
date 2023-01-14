from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *
from .forms import MedicineForm
from django.views.generic import CreateView,ListView,DeleteView,UpdateView

# Create your views here.

class  MedicineView(ListView):
    model = Medicine
    template_name = ''
    
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    
