from typing import Any, Dict
from django import forms

class UserSingup(forms.Form):
    User_Name = forms.CharField(label='Name')
    Password = forms.CharField(label='Password', widget=forms.PasswordInput)
    Cnf_Password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    def clean(self):
        total_cleaned_data = super().clean()
        pwd = total_cleaned_data['Password']
        cnfpwd = total_cleaned_data['Cnf_Password']
        if pwd !=cnfpwd:
            raise forms.ValidationError('Password and Confirm Password Must Be Same!')