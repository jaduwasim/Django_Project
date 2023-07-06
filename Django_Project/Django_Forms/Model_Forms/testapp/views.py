from django.shortcuts import render
from .models import Employee
from .forms import EmployeeForm
# Create your views here.

def Employee_Form_View(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            print('Inserted data:')
            print('Employee No:',form.cleaned_data['Employee_No'])
            print('Employee Nanme:',form.cleaned_data['Employee_Name'])
            print('Employee Salary:',form.cleaned_data['Employee_Salary'])
            print('Employee Address:',form.cleaned_data['Employee_Address'])
            form.save(commit=True)
            return render(request, 'testapp/thanks.html')
    return render(request, 'testapp/home.html', {'form':form})

def Thanks_View(request):
    return render(request, 'testapp/thanks.html')