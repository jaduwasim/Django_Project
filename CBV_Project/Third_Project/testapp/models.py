from django.db import models
from django.urls import reverse

# Create your models here.
class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=64)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=64)

    def __str__(self):
        return self.ename +' '+ self.eaddr

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk':self.pk})