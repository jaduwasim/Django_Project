from django import forms
from .models import To_Do_Model

class To_Do_Form(forms.ModelForm):
    class Meta:
        model = To_Do_Model
        fields = '__all__'