from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .models import *
from accounts.models import UserProfile
from .forms import MedicineForm
from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class  MedicineView(LoginRequiredMixin,ListView):
    model = Medicine
    template_name = 'medicine/medlist.html'
    context_object_name = 'meds'
    
    def get_queryset(self, **kwargs):
        return Medicine.objects.filter(self.request.user).order_by('-tracked_medicine')
    
    """We can however use context data 
    
    def get_context_data(self, **kwargs):
    context = super(Medicine, self).get_context_data(self, **kwargs)
    context[meds] = context.self.request.user.order_by(-tracked_medicine)
    return context"""


    
    
    
   
    
    
