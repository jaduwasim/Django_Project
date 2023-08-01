from django.shortcuts import render, redirect
from .models import To_Do_Model
from .forms import To_Do_Form

# Create your views here.

def Home_View(request):
    data = To_Do_Model.objects.all()
    return render(request, 'todo_app/home.html', {'data':data})

def Add_Data(request):
    form = To_Do_Form
    if request.method == 'POST':
        form = To_Do_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'todo_app/forms.html',{'forms':form})

def Update_data_view(request,id):
    data = To_Do_Model.objects.get(id=id)
    form = To_Do_Form(instance=data)
    if request.method == 'POST':
        form = To_Do_Form(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'todo_app/forms.html',{'forms':form})

def delete_data_view(request, id):
    data = To_Do_Model.objects.get(id=id)
    data.delete()
    return redirect('/')