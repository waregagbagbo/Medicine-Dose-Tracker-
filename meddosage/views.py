from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .models import *
from accounts.models import *
from accounts.models import UserProfile
from .forms import MedicineForm
from django.views.generic import CreateView,ListView,DeleteView,UpdateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class  MedicineView(LoginRequiredMixin,ListView):
    model = Medicine
    template_name = 'medicine/medlist.html'       
    
    def get_context_data(self, **kwargs):
        context = super(MedicineView,self).get_context_data(**kwargs)
        #context['meds'] = Medicine.objects.filter().order_by('-tracked_medicine')
        context['meds'] = Medicine.objects.all()
        return context


class MedicineCreate(CreateView):
    model = Medicine
    template_name = 'medicine/create.html'
    form_class = MedicineForm
    success_url = reverse_lazy('home')    
    
        
        
class MedicineUpdate(UpdateView):  # for edit
    model = Medicine
    template_name = 'medicine/update.html'
    form_class = MedicineForm
    success_url = reverse_lazy('home')
    
    
class MedicineEditView(DetailView):  # for  itemview
    model = Medicine
    template_name = 'medicine/edit.html'
    for_class = MedicineForm  
    
class MedicineDelete(DeleteView):     # for delete
    model = Medicine
    template_name ='medicine/delete.html'
    success_url = reverse_lazy('home')
    

     
    
   
    
    
