from django.shortcuts import render
from testapp.forms import LoginForm
import datetime

# Create your views here.
def home(request):
    form = LoginForm()
    return render(request, 'testapp/home.html', {'forms':form})

def second(request):
    name = request.GET['name']
    response = render(request, 'testapp/second.html', {'name':name})
    response.set_cookie('name',name)
    return response

def result(request):
    name = request.COOKIES['name']
    date = datetime.datetime.now()
    return render(request, 'testapp/result.html', {'name':name, 'date':date})
