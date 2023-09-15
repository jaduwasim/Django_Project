from django.shortcuts import render
from testapp.forms import AdditemForm

# Create your views here.
def home(request):
    return render(request, 'testapp/home.html')

def AddItem(request):
    form = AdditemForm()
    response = render(request, 'testapp/additem.html', {'forms':form})
    if request.method == 'POST':
        form = AdditemForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['Item_Name']
            quntity = form.cleaned_data['Item_Quantity']
            response.set_cookie(name, quntity, 180)
    return response


def Show_Item(request):
    return render(request, 'testapp/showitem.html')