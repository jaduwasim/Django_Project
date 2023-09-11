from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # 10/0
    print()
    print('*'*80)
    print('View funcion')
    return HttpResponse('<h1>Hello World</h1>')