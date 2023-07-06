from django.db import models

# Create your models here.
class NameModel(models.Model):
    Name = models.CharField(max_length=64)

class AgeModel(models.Model):
    Age = models.IntegerField()

class GFModel(models.Model):
    GF_Name = models.CharField(max_length=64)