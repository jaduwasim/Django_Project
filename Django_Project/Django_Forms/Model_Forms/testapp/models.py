from django.db import models

# Create your models here.
class Employee(models.Model):
    Employee_No = models.IntegerField()
    Employee_Name = models.CharField(max_length=64)
    Employee_Salary = models.FloatField()
    Employee_Address = models.CharField(max_length=64)

    class Meta:
        db_table = 'Employee'