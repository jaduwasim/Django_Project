from django.contrib import admin
from .models import Employee

# Register your models here.
class Employee_Admin(admin.ModelAdmin):
    list_display = ['eno','ename','esal','eaddr']

admin.site.register(Employee, Employee_Admin)