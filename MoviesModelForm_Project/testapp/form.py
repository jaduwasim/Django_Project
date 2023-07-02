from django import forms
from testapp.models import Movies_Model

class Movie_Forms(forms.ModelForm):
    class Meta:
        model = Movies_Model
        fields = '__all__'