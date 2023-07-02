from django.shortcuts import render
from . import forms

# Create your views here.
def Student_form_views(request):
    form = forms.StudentForm()
    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        form.is_valid()
        form.save()
        return render(request, 'testapp/thanks.html')
    return render(request, 'testapp/form.html', {'form':form})