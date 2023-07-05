from django.shortcuts import render
from .forms import EmployeeForm
# Create your views here.

def Form_View(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            print('The Entered Data')
            print('Employee No:', form.cleaned_data['Employee_No'])
            print('Employee Name:', form.cleaned_data['Employee_Name'])
            print('Employee No:', form.cleaned_data['Employee_Salary'])
            print('Employee No:', form.cleaned_data['Employee_Address'])
    return render(request, 'testapp/home.html', {'form':form})
