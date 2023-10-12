from django.db import models

class student(models.Model):
    id  = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=70)
    roll = models.IntegerField(unique= True, null = False)
    city = models.CharField(max_length=70)
    marks = models.CharField(max_length=70) 
    pass_date = models.DateField()
    admdatetime = models.DateTimeField()

    
    

   