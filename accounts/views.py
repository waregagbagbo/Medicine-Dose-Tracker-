from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *
from .forms import UserRegisterationForm,UpdateProfileForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic import ListView,TemplateView,DetailView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

class CustomRegisterView(SuccessMessageMixin,CreateView):
    template_name = 'pages/register.html'
    form_class = UserRegisterationForm
    success_url = reverse_lazy('accounts:login')    
    success_message = "Account created successfully"
    
    

class CustomLoginPage(LoginView):
    template_name = 'pages/login.html'
    success_url = reverse_lazy('home')
      
    

class CustomLogout(TemplateView):
    template_name = 'pages/logout.html'
    success_url = reverse_lazy('accounts:login')
    
    
class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/profile.html'
    form_class = UpdateProfileForm
    success_url = reverse_lazy('home')

    