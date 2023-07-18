from django.shortcuts import render

def Home_View(request):
    return render(request, 'blog/home.html')

def About_View(request):
    return render(request, 'blog/about.html')

def Contact_View(request):
    return render(request, 'blog/contact.html')

def Dashboard_View(request):
    return render(request, 'blog/dashboard.html')

def Login_View(request):
    return render(request, 'blog/login.html')

def Logout_View(request):
    return render(request, 'blog/logout.html')

def Signup_View(request):
    return render(request, 'blog/singup.html')