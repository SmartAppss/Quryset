from django.contrib import admin
from .models import student
from .models import teacher
# Register your models here.

@admin.register(student)
class studentadmin(admin.ModelAdmin):
    models_display = ['id','name','roll','marks','pass_date']

@admin.register(teacher)
class studentadmin(admin.ModelAdmin):
    models_display = ['name','empnum','city', 'salary','join_date']