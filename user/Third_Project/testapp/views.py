from django.shortcuts import render, HttpResponseRedirect
from .forms import SingupForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.

# User Registration
def SignupView(request):
    if not request.user.is_authenticated:
        form = SingupForm()
        if request.method == 'POST':
            form = SingupForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your Account Created!!')
                return render(request, 'testapp/thanks.html')
        return render(request, 'testapp/singup.html',{'forms':form})
    else:
        messages.info(request, 'You are alredy Login')
        return render(request, 'testapp/profile.html')


# User Logoin
def UserLogin(request):
    if not request.user.is_authenticated:
        form = AuthenticationForm()
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Your Are Login!!')
                    return render(request, 'testapp/profile.html')
        return render(request, 'testapp/userlogin.html', {'forms':form})
    else:
        messages.info(request, 'You are already Login')
        return render(request, 'testapp/profile.html')

# User Logout
def UserLogout(request):
    logout(request)
    return render(request, 'testapp/userlogin.html')