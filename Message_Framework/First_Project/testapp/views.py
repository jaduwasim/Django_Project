from django.shortcuts import render
from .models import Student
from .forms import StudentForm
from django.contrib import messages
# Create your views here.

def Student_View(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.add_message(request, messages.success, 'You Account Created!!')
            messages.success(request, 'Account Created!!')
    else:
        form = StudentForm()
    return render(request, 'testapp/registration.html', {'form':form})