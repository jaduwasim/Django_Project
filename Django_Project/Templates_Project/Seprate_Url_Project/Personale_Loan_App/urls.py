from django.urls import path
from .views import Personal_Loan

urlpatterns = [
    path('', Personal_Loan)
]
