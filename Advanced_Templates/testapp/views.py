from django.shortcuts import render

# Create your views here.
def Templates_Views(request):
    return render(request, 'testapp/home.html')