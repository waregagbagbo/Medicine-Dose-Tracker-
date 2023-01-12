from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from .views import CustomLoginPage,CustomRegisterView

urlpatterns=[
    path('', CustomLoginPage.as_view(), name='login'),
    path('register/',CustomRegisterView.as_view(), name='register'),
]
