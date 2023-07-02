from django.contrib import admin
from testapp.models import Movies_Model
# Register your models here.

class Movie_Admin(admin.ModelAdmin):
    list_display = ['rdate','Movie_Name','Hero_Name','Heroine_Name','Rating']

admin.site.register(Movies_Model, Movie_Admin)
