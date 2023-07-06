from .models import NameModel, AgeModel, GFModel
from django import forms

class NameForm(forms.ModelForm):
    class Meta:
        model = NameModel
        fields = '__all__'

class AgeForm(forms.ModelForm):
    class Meta:
        model = AgeModel
        fields = '__all__'
    
class GFForm(forms.ModelForm):
    class Meta:
        model = GFModel
        fields = '__all__'