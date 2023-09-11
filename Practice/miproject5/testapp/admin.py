from django.contrib import admin
from testapp.models import Employee

# Register your models here.
# @admin.register(Employee)
class Employee_Admin(admin.ModelAdmin):
    list_display = ['id','eno','ename','esal','eaddr']

admin.site.register(Employee, Employee_Admin)