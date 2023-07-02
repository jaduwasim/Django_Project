from django.db import models

# Create your models here.
class Movies_Model(models.Model):
    class Meta:
        db_table = 'Movies'
        
    rdate = models.DateField()
    Movie_Name = models.CharField(max_length=65)
    Hero_Name = models.CharField(max_length=65)
    Heroine_Name = models.CharField(max_length=65)
    Rating = models.IntegerField()

    
