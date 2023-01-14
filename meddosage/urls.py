from django.urls import path
from .import views
from .views import MedicineView


urlpatterns =[
    path('home',MedicineView.as_view(), name='home'),    
]