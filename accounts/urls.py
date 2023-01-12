from django.urls import path
from .import views
from .views import CustomLoginPage,CustomRegisterView

app_name ='accounts'

urlpatterns=[
    path('', CustomLoginPage.as_view(), name='login'),
    path('register/',CustomRegisterView.as_view(), name='register'),
]
