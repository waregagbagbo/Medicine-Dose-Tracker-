from django.urls import path
from .import views
from .views import CustomLoginPage,CustomRegisterView,CustomLogout,PasswordChangeView

app_name ='accounts'

urlpatterns=[
    path('', CustomLoginPage.as_view(), name='login'),
    path('register/',CustomRegisterView.as_view(), name='register'),
    path('logout', CustomLogout.as_view(), name='logout'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),    
    path('profile',views.profile, name='profile'),
]
