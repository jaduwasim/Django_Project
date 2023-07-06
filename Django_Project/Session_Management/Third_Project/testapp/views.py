from django.shortcuts import render
from .forms import NameForm, AgeForm, GFForm

# Create your views here.

def Home_View(request):
    form = NameForm()
    return render(request, 'testapp/home.html', {'form':form})

def Age_View(request):
    name = request.GET['name']
    form = AgeForm()
    response = render(request, 'testapp/age.html', {'form':form, 'name':name})
    response.set_cookie('name',name)
    return response

def GF_View(request):
    print('Cookies:', request.COOKIES)
    name = request.COOKIES['name']
    age = request.GET['age']
    print(f'age: {age}')
    form = GFForm()
    response = render(request, 'testapp/gf.html', {'form':form, 'name':name})
    response.set_cookie('age',age)
    return response

def Results_View(request):
    print('data:', request.COOKIES)
    name = request.COOKIES['name']
    age = request.COOKIES['age']
    gf = request.GET['gf']
    response = render(request, 'testapp/result.html', {'name':name,'age':age, 'gf':gf})
    response.set_cookie('gf',gf)
    return response