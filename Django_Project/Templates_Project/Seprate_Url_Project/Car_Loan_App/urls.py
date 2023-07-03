from django.urls import path
from .views import Car_Loan

urlpatterns = [
    path('home/', Car_Loan)
]