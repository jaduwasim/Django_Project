from django.db import models

# Create your models here.
class Employee(models.Model):
    rdate = models.DateField()
    movie_name = models.CharField(max_length=64)
    hero_name = models.CharField(max_length=64)
    heroine_name = models.CharField(max_length=64)
    rating = models.IntegerField()

    class Meta:
        db_table = 'Employee'