from rest_framework import serializers # used to convert python objects to JSON
from .models import Medicine
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import serializers

class MedicineSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Medicine
        fields = ('tracked_medicine','dosage','frequency')  

           
        
       
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
        
        
    
class LoginSerializer(serializers.Serializer):
    # serializer defining two field for authentication
    # username and password
    username = serializers.CharField(label="Username", write_only=True)
    password = serializers.CharField(label="Password", style={'input_type': 'password'}, trim_whitespace=False, write_only=True)
    
    
    def validate(self, attrs):
        # take username and password from request
        username = attrs.get('username')
        password = attrs.get('password')
        
        if username and password:
            # try to authenticate the user using Django auth
            user = authenticate(request=self.context.get('request'),username=username, password=password)
            
        if not user:
            # absence of regular user, raise an error
            msg ='Access denied: wrong username or password'
            raise serializers.ValidationError(msg, code='authorization')
        
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        
        # Presence of valid user, put itt in the serializers validated_data
        # Essential to be used in the views
        attrs['user'] = user      
        return super().validate(attrs)
    