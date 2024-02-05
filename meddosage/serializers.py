from rest_framework import serializers # used to convert python objects to JSON
from .models import Medicine
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class MedicineSerializer(serializers.ModelSerializer):
    #model serializer provides a faster way get model field in serialized manner.works as forms
    #user = serializers.ReadOnlyField(source = 'user.username')    
    class Meta:
        model = Medicine
        fields = '__all__'
       #fields = ('tracked_medicine','dosage','frequency',)
        
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username','email','password',)
        extra_kwargs = {'password':{'write_only':True}}
        
        
        def create(self,validated_data):
            user = User(email =validated_data['email'],username = validated_data['username'])
            user.set_password(validated_data['password'])
            user.save()
            Token.objects.create(user=user) # create tokens when user is created
            return user
        