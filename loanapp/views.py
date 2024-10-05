from django.shortcuts import render
from joblib import load
model = load('./savemodel/model.joblib')
# Create your views here.
def pre(request):
    return render(request,'main.html')
def User(request):
    Gender = request.GET['Gender']
    Married = request.GET['Married']
    Dependents = request.GET['Dependents']
    Education = request.GET['Education']
    Self_Employed = request.GET['Self_Employed']
    ApplicantIncome = request.GET['ApplicantIncome']
    CoapplicantIncome = request.GET['CoapplicantIncome']
    LoanAmount = request.GET['LoanAmount']
    Loan_Amount_Term = request.GET['Loan_Amount_Term']
    Credit_History = request.GET['Credit_History']
    Property_Area = request.GET['Property_Area']
    
    Y_predict = model.predict([[Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]])
    if Y_predict[0] == 0:
        Y_predict ="No"
    else:
        Y_predict ="yes"

    
    return render(request,'user.html',{'user' : Y_predict})
