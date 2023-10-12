from django.shortcuts import render
#from datetime import time,date
#from django.db.models import Avg, Sum, Max, Count, Min
from django.db.models import Q

# Create your views here.
from .models import student



def home(request):

#  student_data = student.objects.all()
#  student_data = student.objects.filter(name__exact = 'raman')
#  student_data = student.objects.filter(name__contains = 'a')
#  student_data = student.objects.filter(name__icontains = 'A')
#  student_data = student.objects.filter(id__in = [1,5,4])
#  student_data = student.objects.filter(marks__gt = 80)
#  student_data = student.objects.filter(marks__gte = 80)
#  student_data = student.objects.filter(marks__lt = 80)
#  student_data = student.objects.filter(marks__lte = 80)
#  student_data = student.objects.filter(marks__lte = 80)
#  student_data = student.objects.filter(city__startswith = 'b')
#  student_data = student.objects.filter(city__istartswith = 'B')
#  student_data = student.objects.filter(city__endswith = 'i')
#  student_data = student.objects.filter(city__iendswith = 'I')
#  student_data = student.objects.filter(pass_date__range= ('2023-09-20', '2023-09-27'))
#  student_data = student.objects.filter(admdatetime__date= date(2023 ,5, 23))
#  student_data = student.objects.filter(admdatetime__date__lt= date(2023 ,5, 23))
#  student_data = student.objects.filter(admdatetime__year= 2023)
#  student_data = student.objects.filter(admdatetime__year__gte= 2023)
#  student_data = student.objects.filter(pass_date__month= 9)
#  student_data = student.objects.filter(pass_date__month__gt= 9)
#  student_data = student.objects.filter(pass_date__day__gt= 3)
#  student_data = student.objects.filter(pass_date__week= 37)
#  student_data = student.objects.filter(pass_date__week_day= 3)
#  student_data = student.objects.filter(pass_date__quarter= 2)
#  student_data = student.objects.filter(admdatetime__time__lt= time(10,00))
#  student_data = student.objects.filter(admdatetime__hour__gt= 5)
#  student_data = student.objects.filter(admdatetime__minute__gt= 16)
#  student_data = student.objects.filter(admdatetime__second__gt= 16)
#  student_data = student.objects.filter(pass_date__isnull = False)
####################AGREGATE FUNTION ##################################
#  student_data =  student.objects.all()
#  average =  student_data.aggregate(Avg('marks'))
#  maximum =  student_data.aggregate(Max('marks'))
#  minimum =  student_data.aggregate(Min('marks'))
#  sum =  student_data.aggregate(Sum('marks'))
#  count = student_data.aggregate(Count('marks'))



 
 

#  context = {'stud': student_data, 'average': average, 'maximum': maximum, 'minimum': minimum, 'sum':sum, 'count':count }

################### Q OBJECTS #############################################
 student_data = student.objects.filter(Q(marks__gt= 60) | Q(id__lt = 5)) 
 student_data = student.objects.filter(Q(marks__gt= 60) & Q(id__lt = 5)) 
 
 print('queryset', student_data.query)
 return render(request, 'lookupapp/home.html', {'stud':student_data})