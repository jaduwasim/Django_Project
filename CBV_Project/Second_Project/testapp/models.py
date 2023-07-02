from django.db import models
from django.urls import reverse

# Create your models here.
class Employee_Model(models.Model):

    eno = models.IntegerField()
    ename = models.CharField(max_length=45)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=45)
    # def __str__(self):
    #     return self.name
    def get_absolute_url(self):
        return reverse('emplist', kwargs={'pk':self.p})
