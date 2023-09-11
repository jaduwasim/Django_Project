from django.contrib import admin
from testapp.models import Manager, Person, Employee
# Register your models here.


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ['id','Name','age','address','eno','salary','exp','team_size']


# admin.site.register(Manager, ManagerAdmin)
admin.site.register(Person)
admin.site.register(Employee)