from django.shortcuts import render
from testapp.models import Employee
# Create your views here.

def index(request):
    # emp_list = Employee.objects.order_by('ename')
    emp_list = Employee.objects.esal_range(10000,15000)
    return render(request, 'testapp/index.html',{'emp_list':emp_list})