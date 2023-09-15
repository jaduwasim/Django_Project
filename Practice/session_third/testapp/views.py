from django.shortcuts import render
from testapp.forms import NameForm, AgeForm, GFForm
# Create your views here.
def home(request):
    f = NameForm()
    return render(request, 'testapp/home.html', {'forms':f})

def age(request):
    name = request.GET['Name']
    a = AgeForm()
    response = render(request, 'testapp/age.html', {'name':name, 'forms':a})
    response.set_cookie('name', name)
    return response

def gf(request):
    name = request.COOKIES['name']
    age = request.GET['Age']
    g = GFForm()
    response = render(request, 'testapp/gf.html', {'name': name, 'forms':g})
    response.set_cookie('age',age)
    return response

def result(request):
    name = request.COOKIES['name']
    age = request.COOKIES['age']
    gf = request.GET['GF_Name']
    response = render(request, 'testapp/result.html',{'name':name, 'age':age, 'gf':gf})
    response.set_cookie('gf',gf)
    return response