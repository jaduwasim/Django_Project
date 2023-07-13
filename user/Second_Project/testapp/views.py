from django.shortcuts import render
from .froms import SingupForm
from django.contrib import messages
# Create your views here.

def SingupView(request):
    form = SingupForm()
    if request.method == 'POST':
        form = SingupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Acount Created !!')
            return render(request, 'testapp/singup.html',{'forms':form})
    return render(request, 'testapp/singup.html',{'forms':form})
