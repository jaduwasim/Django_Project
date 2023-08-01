from django.db import models

# Create your models here.
class To_Do_Model(models.Model):
    Title_Name = models.CharField(max_length=60)
    category = models.CharField(max_length=60)
    description = models.TextField()
    date = models.DateField()

    class Meta:
        db_table ='todo_table'