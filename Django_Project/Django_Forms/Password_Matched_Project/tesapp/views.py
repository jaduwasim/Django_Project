from django.shortcuts import render
from .form import UserSingup
# Create your views here.

def UserSignUp(request):
    form = UserSingup()
    if request.method == 'POST':
        form = UserSingup(request.POST)
        if form.is_valid():
            print('Data', form.cleaned_data)
            print('Name:', form.cleaned_data['User_Name'])
            print('Passwrod:', form.cleaned_data['Password'])
            print('Confirm Password:', form.cleaned_data['Cnf_Password'])
            return render(request, 'testapp/thanks.html')
    return render(request, 'testapp/singup.html', {'form':form})