from django import forms

class NameForm(forms.Form):
    Name = forms.CharField()

class AgeForm(forms.Form):
    Age = forms.IntegerField()

class GFForm(forms.Form):
    GF_Name = forms.CharField()