from django.contrib import admin
from .models import *

# Register your models here.
class MedicineAdmin(admin.ModelAdmin):
    list_display =('tracked_medicine','dosage','frequency')
admin.site.register(Medicine, MedicineAdmin)

