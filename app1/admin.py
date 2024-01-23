from django.contrib import admin
from .models import StuInfo
# Register your models here.



@admin.register(StuInfo)
class Student(admin.ModelAdmin):
    
    list_display = ['id','roll', 'Name', 'Address']
    
    