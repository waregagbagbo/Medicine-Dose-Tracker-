from django.urls import path
from .import views
from .views import MedicineView,MedicineDetail
from rest_framework.authtoken import views
urlpatterns =[
    path('',MedicineView.as_view(), name='home'),
    path('medicine/<int:pk>/', MedicineDetail.as_view(), name='dose_detail'),
    path('api-token-auth/', views.obtain_auth_token)  
    ]
