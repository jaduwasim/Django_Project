from django.contrib import admin
from testapp.models import ContactInfo, Student, Teacher
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','roll','marks']

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','subject','salary']
    

admin.site.register(ContactInfo, ContactAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
