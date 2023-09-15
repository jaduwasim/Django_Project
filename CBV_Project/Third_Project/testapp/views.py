from django.shortcuts import render
from django.views.generic import View, ListView, CreateView, DetailView, UpdateView, DeleteView
# Create your views here.
from .models import Employee
from django.urls import reverse_lazy

class HomeClass(View):
    def get(self, request):
        return render(request, 'testapp/home.html')
    
class ClassListView(ListView):
    model = Employee

class ClassDetailView(DetailView):
    model = Employee

class ClassCreateView(CreateView):
    model = Employee
    fields = '__all__'

class ClassUpdateView(UpdateView):
    model = Employee
    fields = '__all__'

class ClassDeleteView(DeleteView):
    model = Employee
    success_url = reverse_lazy('list')