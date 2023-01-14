from django.db import models

# Create your models here.

class Medicine(models.Model):
    tracked_medicine = models.CharField(max_length=10)
    dosage = models.CharField(max_length=10)
    frequency = models.IntegerField()
        
    class Meta:
        verbose_name = 'Medicine'
        ordering = ['-tracked_medicine']
        
    def __str__(self):
        #return self.tracked_medicine
        return "%s,%s,%s"% self.tracked_medicine, self.dosage, self.frequency
    
    