from django.contrib import admin
from .models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','rdate','movie_name','hero_name','heroine_name','rating']

admin.site.register(Employee, EmployeeAdmin)