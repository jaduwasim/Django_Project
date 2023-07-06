from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

        labels = {"rdate":"Release Date", 
                  'movie_name':'Movie Name', 
                  'hero_name':'Hero Name', 
                  'heroin_name':'Heroine Name', 
                  'rating':'Movie Rating'
                }