from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from testapp.models import Employee_Model
# Create your views here.

class Employee_List(ListView):
    model = Employee_Model

class Employee_Create_View(CreateView):
    model = Employee_Model
    fields = '__all__'

class Employee_Detail_View(DetailView):
    model = Employee_Model

class Employee_Update_View(UpdateView):
    model = Employee_Model
    fields ='__all__'

class Employee_Delete_View(DeleteView):
    model = Employee_Model