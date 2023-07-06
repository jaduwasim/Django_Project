from django.shortcuts import render
from .forms import EmployeeForm
from .models import Employee
# Create your views here.

def index_view(request):
    return render(request, 'testapp/index.html')

def add_view(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index_view(request)
    return render(request,'testapp/add.html',{'form':form})

def list_view(request):
    movie_list = Employee.objects.all().order_by('-rating')
    return render(request, 'testapp/list_movie.html', {'movie_list':movie_list})