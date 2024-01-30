from rest_framework import serializers # used to convert python objects to JSON
from .models import Medicine

class MedicineSerializer(serializers.ModelSerializer):
    # model serializer provides a faster way get model field in serialized manner.works as forms
    class Meta:
        model = Medicine
        fields = '__all__'