from django.urls import path
from .views import Home_Loan

urlpatterns = [
    path('',Home_Loan),
]