from django.shortcuts import render
from testapp.models import Employee, First_Proxy_Emoloyee
# Create your views here.

def index(request):
    emp_list = First_Proxy_Emoloyee.objects.order_by('-eno')
    return render(request, 'testapp/index.html',{'emp_list' : emp_list})
