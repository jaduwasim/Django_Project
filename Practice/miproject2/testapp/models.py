from django.db import models

# Create your models here.

class ContactInfo(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    addr = models.CharField(max_length=64)

    class Meta:
        db_table = 'contact_info'
    
class Student(ContactInfo):
    roll = models.IntegerField()
    marks = models.IntegerField()
    class Meta:
        db_table = 'student'

class Teacher(ContactInfo):
    subject = models.CharField(max_length=64)
    salary = models.FloatField()
    class Meta:
        db_table = 'teacher'