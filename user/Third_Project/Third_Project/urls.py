"""Third_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testapp.views import (SignupView, UserLogin, UserLogout, Change_Pass_View,
                        Change_Second_Pass_View, Profile_View)
from testapp.forms import Forget_Password_Form, SetPasswordForm
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('singup/', SignupView, name='singup'),
    path('login/',UserLogin, name='login'),
    path('logout/', UserLogout, name='logout'),
    path('changepass/', Change_Pass_View, name='changepass'),
    path('changesecondpass/', Change_Second_Pass_View, name='changesecondpass'),
    path('profile/', Profile_View, name='profile'),
    # Forget Password
    path('password-reset/', PasswordResetView.as_view(template_name = 'testapp/forgetpassword.html', form_class = Forget_Password_Form), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name = 'testapp/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name = 'testapp/password_reset_confirm.html', form_class = SetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(template_name='testapp/password_reset_complete.html'), name='password_reset_complete')

]
