from django.db import models

# Create your models here.

class Person(models.Model):
    Name = models.CharField(max_length=64)
    age = models.IntegerField()
    address = models.CharField(max_length=64)
    class Meta:
        db_table = 'person'
class Employee(Person):
    eno = models.IntegerField()
    salary = models.FloatField()
    class Meta:
        db_table = 'employee'
    
class Manager(Employee):
    exp = models.IntegerField()
    team_size = models.IntegerField()
    class Meta:
        db_table = 'manager'