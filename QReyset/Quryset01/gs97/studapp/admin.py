from django.contrib import admin

# Register your models here.
from .models import student

# Register your models here.

@admin.register(student)
class studentadmin(admin.ModelAdmin):
    models_display = ['id','name','roll','marks','pass_date','admdatetime']

