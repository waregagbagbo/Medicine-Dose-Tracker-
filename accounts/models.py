from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True,on_delete=models.CASCADE)
    age = models.CharField(max_length= 15, null=True)
    sex = models.CharField(max_length=10, null=True)
    country = models.CharField(max_length=10, null=True)
    
    class Meta: 
        verbose_name = "Profile"
        
    def __str__(self):
        return '%s'% self.user
    
    
