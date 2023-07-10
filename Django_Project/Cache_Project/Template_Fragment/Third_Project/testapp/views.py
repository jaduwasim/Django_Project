from django.shortcuts import render

# Create your views here.
def Home_View(request):
    return render(request, 'testapp/home.html')