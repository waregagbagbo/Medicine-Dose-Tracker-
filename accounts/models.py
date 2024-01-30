from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True,on_delete=models.CASCADE)
    age = models.CharField(max_length= 15, null=True)
    sex = models.CharField(max_length=10, null=True)
    country = models.CharField(max_length=10, null=True)
    #avatar = models.ImageField(null=True)
    
    
    def save(self, *args, **kwargs):
        #img = Image.open(self.avatar.path)
        super(*args, **kwargs).save()
       
        
        """if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)"""
            
    
    #class Meta: 
        #verbose_name = "Profile"
        
    def __str__(self):
        return '%s'% self.user
    
    
