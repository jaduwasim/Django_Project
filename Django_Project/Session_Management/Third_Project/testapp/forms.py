from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label='Name')

class AgeForm(forms.Form):
    age = forms.CharField(label='Age')

class GFForm(forms.Form):
    gf = forms.CharField(label='Girl Freind Name')
