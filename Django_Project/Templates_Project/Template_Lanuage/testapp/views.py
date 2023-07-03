from django.shortcuts import render

# Create your views here.

def Home_Views(request):
    dic = {'name':'Washim'}
    return render(request, 'testapp/Home_Views.html', dic)