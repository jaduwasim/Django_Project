from django.contrib import admin
from testapp.models import Employee, First_Proxy_Emoloyee
# Register your models here.

@admin.register(Employee)
class Employee_Admin(admin.ModelAdmin):
    list_display = [
        'id','eno','ename','esal','eaddr'
    ]
# admin.site.register(Employee, Employee_Admin)

class First_Proxy_Emoloyee_Admin(admin.ModelAdmin):
    list_display = [
        'id','eno','ename','esal','eaddr'
    ]
admin.site.register(First_Proxy_Emoloyee, First_Proxy_Emoloyee_Admin)