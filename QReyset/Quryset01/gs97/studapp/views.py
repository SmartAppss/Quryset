from django.shortcuts import render

# Create your views here.
from .models import student



def home(request):
 #student_data  = student.objects.get(pk = 1)
#student_data  = student.objects.earliest('pass_date')
#student_data  = student.objects.order_by('marks').first()
#student_data  = student.objects.all()
#student_data  = student.objects.order_by('marks').last()
#print(student_data.exists())
#student_data  = student.objects.create(name = 'vameer', roll =107, marks = 65, city = 'TN', pass_date = '2023-8-7')
#student_data, created  = student.objects.get_or_create(name = 'anush', roll =108, marks = 60, city = 'TN', pass_date = '2023-8-7')
#student_data = student.objects.filter(id =4).update(name = 'kabir', marks = 80)
#student_data = student.objects.filter(marks =60).update(city = 'pass')
#student_data, created = student.objects.update_or_create(id = 5, name = 'sam', defaults= {'name' : 'kohli'})
# stu = [
#     student(name = 'veena', roll =101, marks = 80, city = 'durga', pass_date = '2023-9-8'),
#     student(name = 'reena', roll =102, marks = 60, city = 'durga', pass_date = '2023-9-9'),
#     student(name = 'tinaa', roll =103, marks = 70, city = 'durga', pass_date = '2023-9-12'),
#     student(name = 'sara', roll =104, marks = 40, city = 'durga', pass_date = '2023-9-14'),
# ]
# student_data = student.objects.bulk_create(stu)
# all_student_data = student.objects.all()
# for stu in all_student_data:
#     stu.city = 'Bhel'
#     student_data = student.objects.bulk_update(all_student_data,['city'])  
#  student_data = student.objects.all()
#  student_data = student.objects.bulk_create(stu)
#  all_student_data = student.objects.all()
#  for stu in all_student_data:
#     stu.city = 'Bhel'
#     student_data = student.objects.bulk_update(all_student_data,['city'])
#  student_data = student.objects.in_bulk([])
#  print(student_data)
#  student_data = student.objects.get(pk =1).delete()
#------------------------------------------------------------------------------------------
############## LOOK-UPS######################################################

 student_data = student.objects.all()
 print(student_data.count()) 
 return render(request, 'studapp/home.html',
                  {'stud':student_data})