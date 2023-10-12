from django.db import models
from django.utils import timezone
# Create your models here.


# Create your models here.

class student(models.Model):
    id  = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=70)
    roll = models.IntegerField(unique= True, null = False)
    city = models.CharField(max_length=70)
    marks = models.CharField(max_length=70) 
    pass_date = models.DateField()
    admdatetime = models.DateTimeField()
    
    

    def __str__(self) -> str:
        return f'{self.name}, {self.roll}, {self.city},{self.marks}'
    