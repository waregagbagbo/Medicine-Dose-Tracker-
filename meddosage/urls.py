from django.urls import path
from .import views
from .views import MedicineView,MedicineDetail

urlpatterns =[
    path('',MedicineView.as_view(), name='home'),
    path('medicine/<int:pk>/', MedicineDetail.as_view(), name='dose_detail'),
       
    ]
