from django.contrib import admin
from .models import To_Do_Model
# Register your models here.

@admin.register(To_Do_Model)
class Todo_Admin(admin.ModelAdmin):
    list_display = ['id','Title_Name','category','description','date']

# admin.site.register(To_Do_Model, Todo_Admin)