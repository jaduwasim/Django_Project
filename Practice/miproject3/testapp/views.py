from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def test(request):
    print('Views Logic Exicution')
    print(10/0)
    return HttpResponse(
        '<h1>Hello World</h1>'
    )