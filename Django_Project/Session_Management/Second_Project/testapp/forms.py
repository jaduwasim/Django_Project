from django import forms

class Name_Form(forms.Form):
    name = forms.CharField(label='Name')