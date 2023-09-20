from django.db import models

# Create your models here.

class Task_Model(models.Model):    
    choices_status = (
        ('Incomplete', 'Incomplete'),
        ('Complete', 'Complete')
    )
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=30, choices=choices_status, default='Incomplete')
      
    
