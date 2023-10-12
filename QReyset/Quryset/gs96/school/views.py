from django.shortcuts import render
from .models import student
from .models import teacher

def home(request):

 #student_data  = student.objects.all()
  student_data  = student.objects.get(pk = 1)
 #student_data = student.objects.order_by('id')
 #student_data = student.objects.order_by('marks').first()
 #student_data = student.objects.order_by('marks').last()
 #student_data = student.objects.earliest('pass_date')
 #student_data  = student.objects.all()
 #print(student_data.exists()) #IT WILL GIVE TURE ARE FALSE 
 #student_data = student.objects.create(name = 'kohli', roll = 106, city = 'dheli', marks = 95, pass_date = '2023-5-6')
 #student_data, create = student.objects.get_or_create(name = 'rohith', roll = 107, city = 'mumbai', marks = 87, pass_date = '2023-5-14')
 #student_data = student.objects.filter(roll = 107).update(name = 'rohan')
 #student_data, create = student.objects.update_or_create(roll = 106, name = 'kohli', defaults= {'name' : 'komal'})
#   stu = [
#   student(name = 'veena', roll = 108, city = 'kochi', marks = 67, pass_date = '2023-5-15'),
#   student(name = 'kavitha', roll = 109, city = 'sikim', marks = 75, pass_date = '2023-5-15'),
#   student(name = 'kamala', roll = 110, city = 'bhupal', marks = 98, pass_date = '2023-5-15'),
#   ]
# #   student_data = student.objects.bulk_create(stu)
#   all_student_data = student.objects.all()
#   for stu in all_student_data:
#     stu.city = 'banglore'
#     student_data = student.objects.bulk_update(all_student_data,['city'])
#tudent_data = student.objects.delete()
#student_data = student.objects.filter(pass_date__month = 5)
#student_data = student.objects.count('marks')
#student_data = student.objects.latest('pass_date')
#student_data = student.objects.aget_or_create(name='raj')
#student_data = student.objects.defer('city')
  #student_data = student.objects.filter(marks = 80).distinct()
  #student_data  = student.objects.dates( 'pass_date','year')
  #student_data  = student.objects.filter( roll = 108).delete()
  #student_data  = student.objects.exclude( roll = 105)
  #student_data  = student.objects.order_by( 'roll').reverse()[0:3]
  #student_data  = student.objects.values('id','name')
  #student_data  = student.objects.filter(marks = 80) & student.objects.filter(name = 'raj')
  #student_data  = student.objects.filter(marks = 80) | student.objects.filter(name = 'raj')
#   student_data1  = student.objects.values_list('id','name', named=True) 
#   student_data2  = student.objects.values_list('id','city', named=True) 
#   student_data = student_data2.union(student_data1) 
 # student_data1  = student.objects.values_list('id','name', named=True) 
 # student_data2  = student.objects.values_list('id','name', named=True) 
  #student_data = student_data2.intersection(student_data1) 
#   student_data1  = student.objects.values_list('id','name', named=True) 
#   student_data2  = student.objects.values_list('id','name', named=True) 
#   student_data = student_data2.difference(student_data1) 

  
  

  print("update1", student_data)
  #print("get", create) # it will return  get false
  return render(request, 'school/home.html',
                  {'studs':student_data})
