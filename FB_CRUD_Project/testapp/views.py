from django.shortcuts import render, redirect
from .form import Employee_Form
from testapp.models import Employee

# Create your views here.


# Inserting Data in Tables (C:Create)
def Employee_Views(request):
    forms = Employee_Form()
    if request.method == 'POST':
        forms = Employee_Form(request.POST)
        if forms.is_valid():
            forms.save()
        return redirect('/')
    return render(request, 'testapp/form.html', {'form':forms})

# Retrive all Data(R: Retrive)
def Employee_List(request):
    emp_list = Employee.objects.all()
    return render(request,'testapp/emp_list.html',{'emp_list':emp_list})

# Retrive a Single Records
def Employee_Single_Record(request,id):
    emp = Employee.objects.get(id=id)
    return render(request, 'testapp/single_data.html',{'emp':emp})

# Update a existing records
def Employee_Update_Views(request, id):
    emp = Employee.objects.get(id=id)
    form = Employee_Form(instance=emp)
    if request.method == 'POST':
        form = Employee_Form(request.POST , instance=emp) # if we are not take instance=emp then new record will be generate
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'testapp/form.html', {'form':form})

# Delete an existing record
def Employee_Delete_Views(request, id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return redirect('/')