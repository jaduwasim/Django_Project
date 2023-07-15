from django.shortcuts import render, HttpResponseRedirect
from .forms import SingupForm, Passwor_Change_Form, EditUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
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
                    return HttpResponseRedirect('/profile/')
        return render(request, 'testapp/userlogin.html', {'forms':form})
    else:
        messages.info(request, 'You are already Login')
        return HttpResponseRedirect('/profile/')

# Profile Update
def Profile_View(request):
    if request.user.is_authenticated:
        form = EditUserForm(instance=request.user)
        if request.method == 'POST':
            form = EditUserForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.info(request, 'Your Profile Updated Succesfull!!')
        return render(request, 'testapp/profile.html',{'forms':form})
    else:
        messages.info(request, 'Please Login First')
        return render(request, 'testapp/userlogin.html')
# User Logout
def UserLogout(request):
    logout(request)
    messages.info(request, 'You Logout Succefully!!')
    return render(request, 'testapp/userlogin.html')

# Change Password with Asking Old Password
def Change_Pass_View(request):
    if request.user.is_authenticated:
        form = Passwor_Change_Form(user=request.user)
        if request.method == 'POST':
            form = Passwor_Change_Form(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user) #it will maintain login session
                messages.info(request, 'Your Password has been changed!!')
                return render(request, 'testapp/profile.html')
        return render(request, 'testapp/passwordchange.html', {'forms':form})
    else:
        messages.info(request, 'Please Login First')
        return render(request,'testapp/userlogin.html')
    
# Chagne Password Without Asking Old Password
def Change_Second_Pass_View(request):
    if request.user.is_authenticated:
        form = SetPasswordForm(user=request.user)
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user) #it will maintain login session
                messages.info(request, 'Your Password has been changed!!')
                return render(request, 'testapp/profile.html')
        return render(request, 'testapp/passwordchange.html', {'forms':form})
    else:
        messages.info(request, 'Please Login First')
        return render(request,'testapp/userlogin.html')