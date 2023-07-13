from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def singup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Account Created Succes!!')
            return render(request, 'testapp/singup.html', {'forms':form})
    return render(request, 'testapp/singup.html', {'forms':form})
