from django.shortcuts import render
from .froms import NameForm, AgeForm, GFForm
# Create your views here.

def Home(request):
    form = NameForm()
    return render(request,'testapp/home.html', {'form':form})

def Age_View(request):
    name = request.GET['Name']
    form = AgeForm()
    response = render(request,'testapp/age.html', {'form':form, 'name':name})
    response.set_cookie('name',name)
    return response

def GF_View(request):
    age = request.GET['Age']
    name = request.COOKIES['name']
    form = GFForm()
    response = render(request,'testapp/gf.html', {'form':form, 'name':name})
    response.set_cookie('age',age)
    return response

def Result_View(request):
    name = request.COOKIES['name']
    age = request.COOKIES['age']
    gf = request.GET['GF_Name']
    response = render(request,'testapp/result.html', {'name':name, 'age':age,'gf':gf})
    response.set_cookie('gf',gf)
    return response