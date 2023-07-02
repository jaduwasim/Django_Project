from django.shortcuts import render

# Create your views here.
def Template_Views(request):
    return render(request, 'testapp/home.html')