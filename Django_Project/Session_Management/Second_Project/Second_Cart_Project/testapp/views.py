from django.shortcuts import render
from .forms import AddItemForm

# Create your views here.

def AddItemView(request):
    form = AddItemForm()
    if request.method == 'POST':
        name = request.POST['name']
        quantity = request.POST['quantity']
        request.session[name]=quantity
        request.session.set_expiry(120)
    return render(request, 'testapp/additem.html', {'form':form})

def DisplayView(request):
    return render(request, 'testapp/displayitem.html')