from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()
    city = models.CharField(max_length=70)
    marks = models.CharField(max_length=70)
    pass_date = models.DateField( null= True)

    def __str__(self) -> str:
        return f'{self.name, self.roll, self.city,self.marks}'
    

class teacher(models.Model):
    name = models.CharField(max_length=70)
    empnum = models.IntegerField(unique= True, null=False)
    city = models.CharField(max_length=70)
    salary = models.CharField(max_length=70)
    join_date = models.DateField()