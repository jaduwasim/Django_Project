from django.shortcuts import render
from .models import Employee
# Create your views here.
def Home_View(request):
    emp_list = Employee.objects.all()
    mydic = {'emp_list':emp_list}
    return render(request, 'testapp/home.html', mydic)
