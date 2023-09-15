from django.urls import path
from testapp import views


urlpatterns =[
    path('', views.home),
    path('second/', views.second),
    path('result/', views.result)
]