from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields ='__all__'

        labels = {
            'name':'Enter Name',
            'password':'Password',
            'mail':'Email'
        }