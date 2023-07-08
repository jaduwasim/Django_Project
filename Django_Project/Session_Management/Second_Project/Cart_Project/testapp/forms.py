from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label='NAME')

class AgeForm(forms.Form):
    Age = forms.IntegerField(label='AGE')

class GFForm(forms.Form):
    gf = forms.CharField(label='GF NAME')