from django.shortcuts import render

# Create your views here.
def First_View(request):
    return render(request, 'testapp/first_views.html')

def Second_Views(request):
    return render(request, 'testapp/second_views.html')