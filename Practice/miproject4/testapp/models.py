from django.db import models

# Create your models here.

class Parent_One(models.Model):
    feild_one = models.CharField(max_length=64)
    feild_two = models.CharField(max_length=64)

class Parent_Second(models.Model):
    feild_three = models.CharField(max_length=64, primary_key = True)
    feild_fourth = models.CharField(max_length=64)


class Child(Parent_One, Parent_Second):
    feild_five = models.CharField(max_length=64)
    feild_six = models.CharField(max_length=64)
