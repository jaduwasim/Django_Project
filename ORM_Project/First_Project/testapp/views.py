from django.shortcuts import render
from .models import Student
# Create your views here.
def home(request):
    student_data = Student.objects.filter(name__contains ='म')
    return render(request, 'testapp/home.html', {'students':student_data})