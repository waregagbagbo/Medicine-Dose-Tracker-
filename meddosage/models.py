from django.db import models
from accounts.models import UserProfile

# Create your models here.

class Medicine(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    tracked_medicine = models.CharField(max_length=10, null=True)
    dosage = models.CharField(max_length=10, null=True)
    frequency = models.IntegerField()
        
    class Meta:
        verbose_name = 'Medicine'
        ordering = ['-tracked_medicine']
        
    def __str__(self):
        #return self.tracked_medicine
        return "%s,%s,%s"% self.tracked_medicine, self.dosage, self.frequency
    
    