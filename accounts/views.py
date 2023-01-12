from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *
from .forms import UserRegisterationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic import ListView,TemplateView,DetailView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

class CustomRegisterView(SuccessMessageMixin,CreateView):
    template_name = 'accounts/register.html'
    form_class = UserRegisterationForm
    success_url = reverse_lazy('login')    
    success_message = "Account created successfully"
    
    

class CustomLoginPage(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy()
    
    def get_success_url(self):
        return self.get_redirect_url() or self.get_default_redirect_url()
    

    