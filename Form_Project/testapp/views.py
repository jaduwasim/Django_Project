from django.shortcuts import render
from . import forms

# Create your views here.
def Form_Views(request):
    form = forms.StudentForm()
    if request.method=='POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            print('Form Validation Success printing Data:')
            print('Name:',form.cleaned_data['name'])
            print('Marks:',form.cleaned_data['marks'])

    return render(request, 'testapp/base.html',{'form':form})
