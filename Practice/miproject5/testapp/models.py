from django.db import models
from django.db.models.query import QuerySet

# Create your models here.

class CustomManage(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-ename')

    def order_by(self, param):
        return super().get_queryset().order_by(param)
    
    def esal_range(self, min, max):
        return super().get_queryset().filter(esal__range= (min, max))
    

class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=64)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=64)
    objects = CustomManage()

    class Meta:
        db_table = 'employee'