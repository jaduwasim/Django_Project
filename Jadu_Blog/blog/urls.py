from django.urls import path
from blog import views

urlpatterns = [
    path('',views.Home_View, name='home'),
    path('about/',views.About_View, name='about'),
    path('contact/',views.Contact_View, name='contact'),
    path('dashboard/',views.Dashboard_View, name='dashboard'),
    path('login/',views.Login_View, name='login'),
    path('signup/',views.Signup_View, name='singup'),
    path('logout/',views.Logout_View, name='logout'),   
]