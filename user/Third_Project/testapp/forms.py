from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django import forms

class SingupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
    
class Passwor_Change_Form(PasswordChangeForm):
    old_password = forms.CharField(label='Enter Your Old Password', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput)

class EditUserForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','date_joined','last_login']
        labels = {'email':'Email'}

class Forget_Password_Form(PasswordResetForm):
    email = forms.EmailField(label='Email', max_length=265 , widget=forms.EmailInput)

class Password_Set_Form(SetPasswordForm):
    new_password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)