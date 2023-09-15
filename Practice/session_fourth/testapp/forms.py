from django import forms

class AdditemForm(forms.Form):
    Item_Name = forms.CharField()
    Item_Quantity = forms.IntegerField()