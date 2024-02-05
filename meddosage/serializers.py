from rest_framework import serializers # used to convert python objects to JSON
from .models import Medicine
from django.contrib.auth.models import User

class MedicineSerializer(serializers.ModelSerializer):
    #model serializer provides a faster way get model field in serialized manner.works as forms
    #user = serializers.ReadOnlyField(source = 'user.username')    
    class Meta:
        model = Medicine
        fields = ' __all__'
       #fields = ('tracked_medicine','dosage','frequency',)
        