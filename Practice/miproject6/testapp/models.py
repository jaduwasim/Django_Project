from typing import Any
from django.db import models
from django.db.models.query import QuerySet

# Create your models here.

class CustomModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('ename')

    def order_by(self, param):
        return super().get_queryset().order_by(param)

class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=64)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=64)

    class Meta:
        db_table = 'employee'
    
class First_Proxy_Emoloyee(Employee):
    objects = CustomModelManager()
    class Meta:
        proxy = True