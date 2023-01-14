from django.urls import path
from .import views
from .views import MedicineView

app_name = 'meddosage'

urlpatterns =[
    path('home',MedicineView.as_view(), name='medics'),    
]