from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SingupForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name', 'email']
