from django.contrib import admin
from testapp.models import Parent_One, Parent_Second, Child
# Register your models here.


@admin.register(Parent_One)
class Parent_One_Admin(admin.ModelAdmin):
    list_display = ['id','feild_one','feild_two']

class Parent_Second_Admin(admin.ModelAdmin):
    list_display = ['feild_three','feild_fourth']
admin.site.register(Parent_Second, Parent_Second_Admin)

class Child_Admin(admin.ModelAdmin):
    list_display = ['id','feild_one','feild_two','feild_three','feild_fourth','feild_five','feild_six']

admin.site.register(Child, Child_Admin)