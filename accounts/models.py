from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=10 ,blank=True, null=True)
    
    class Meta: 
        verbose_name = "Profile"
        
    def __str__(self):
        return '%s'% self.user
    
    
