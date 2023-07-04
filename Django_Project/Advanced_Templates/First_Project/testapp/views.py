from django.shortcuts import render
from .models import Employee

# Create your views here.
def Home_View(request):
    emp_list = Employee.objects.all()
    return render(request, 'testapp/home.html', {'emp_list':emp_list})