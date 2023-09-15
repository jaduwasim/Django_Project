from django.urls import path
from testapp import views

urlpatterns = [
    path('', views.home),
    path('age/', views.age),
    path('gf/', views.gf),
    path('result/', views.result)
]