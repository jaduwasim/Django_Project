from django.shortcuts import render

# Create your views here.
def Personal_Loan(request):
    return render(request, 'Personale_Loan_App/personal_loan.html')