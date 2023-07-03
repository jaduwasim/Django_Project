from django.shortcuts import render

# Create your views here.

def Car_Loan(request):
    return render(request,'Car_Loan_App/car_loan.html')