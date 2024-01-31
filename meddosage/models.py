from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Medicine(models.Model):
    user = models.ForeignKey('auth.User',null=True, on_delete=models.CASCADE)
    tracked_medicine = models.CharField(max_length=10, null=True)
    dosage = models.CharField(max_length=20, null=True)
    frequency = models.IntegerField(null=True)
        
    class Meta:
        verbose_name = 'Medicine'
        ordering = ['-tracked_medicine']
        
    def __str__(self):
        #return self.tracked_medicine
        return "%s,%s,%s"% (self.tracked_medicine,self.dosage, self.frequency)
    
    