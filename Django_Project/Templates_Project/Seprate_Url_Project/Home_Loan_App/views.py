from django.shortcuts import render

# Create your views here.
def Home_Loan(request):
    return render(request, 'Home_Loan_App/home_loan.html')