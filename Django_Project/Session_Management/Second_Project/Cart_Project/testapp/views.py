from django.shortcuts import render
from .forms import NameForm, AgeForm, GFForm

# Create your views here.

def NameView(request):
    form = NameForm()
    return render(request, 'testapp/name.html',{'form':form})

def AgeView(request):
    name = request.GET['name']
    request.session['name'] = name
    form = AgeForm()
    return render(request, 'testapp/age.html', {'form':form})

def GFView(request):
    age = request.GET['Age']
    request.session['Age'] = age
    form = GFForm()
    return render(request, 'testapp/gf.html',{'form':form})

def ResultView(request):
    gf = request.GET['gf']
    request.session['gf'] = gf
    request.session.set_expiry(60)
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    return render(request, 'testapp/result.html')