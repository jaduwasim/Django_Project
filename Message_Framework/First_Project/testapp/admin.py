from django.contrib import admin
from .models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','password','mail']

admin.site.register(Student, StudentAdmin)