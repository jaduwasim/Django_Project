from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    mail = models.EmailField()

    class Meta:
        db_table = 'Student'