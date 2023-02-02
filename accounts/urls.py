from django.urls import path
from .import views
from .views import CustomLoginPage,CustomRegisterView,CustomLogout,UserProfileView

app_name ='accounts'

urlpatterns=[
    path('', CustomLoginPage.as_view(), name='login'),
    path('register/',CustomRegisterView.as_view(), name='register'),
    path('logout', CustomLogout.as_view(), name='logout'),
    path('profile', UserProfileView.as_view(), name='profile'),
]
