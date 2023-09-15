from django.urls import path
from testapp import views

urlpatterns = [
    path('', views.home),
    path('additem/', views.AddItem),
    path('showitem/', views.Show_Item),
]