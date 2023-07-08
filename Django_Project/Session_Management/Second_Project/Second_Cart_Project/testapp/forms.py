from django import forms

class AddItemForm(forms.Form):
    name = forms.CharField(label='Name')
    quantity = forms.IntegerField(label='Quantity')