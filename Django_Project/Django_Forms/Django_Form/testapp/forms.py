from django import forms
from django.core import validators

def Multiple_Of_Thousend(salary):
    if salary % 1000 != 0:
        raise forms.ValidationError('Salary Sholud be Multiple of Thousend')
    return salary
class EmployeeForm(forms.Form):
    Employee_No = forms.IntegerField()
    Employee_Name = forms.CharField()
    Employee_Salary = forms.FloatField(validators=[Multiple_Of_Thousend])
    Employee_Address = forms.CharField(widget=forms.Textarea)

    def clean_Employee_Name(self):
        name = self.cleaned_data['Employee_Name']
        print(name)
        if len(name) <= 5:
            raise forms.ValidationError('Employee Name Should be take more five character')       
        return name