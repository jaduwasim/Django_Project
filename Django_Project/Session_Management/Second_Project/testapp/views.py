from django.shortcuts import render
from .forms import Name_Form
import datetime

# Create your views here.
def Home_View(request):
    form = Name_Form()
    return render(request,'testapp/home.html', {'form':form})

def Date_and_Time_View(request):
    name = request.GET['name']
    response = render(request, 'testapp/datetime.html', {'name':name})
    response.set_cookie('name', name)
    return response

def Results_View(request):
    print(request.COOKIES)
    name = request.COOKIES['name']
    count = request.COOKIES['count']
    print('count:',count)
    date_time = datetime.datetime.now()
    mydict = {'name':name,'datetime':date_time}
    return render(request, 'testapp/results.html', mydict)
