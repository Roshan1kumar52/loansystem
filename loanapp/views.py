from django.contrib.auth.models import User
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib import messages
from joblib import load

model = load('./savemodel/model.joblib')
# Create your views here.

def sig(request):
    messss=None
    #action="{% url 'loanapp:sign' %}"
 #request.method=='POST' and 
    if  request.method=='POST' and 'Signup' in request.POST:
       
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        name1=request.POST.get('Username')
        emal=request.POST.get('email')
        psw1=request.POST.get('psw')
        user=User.objects.create_user(first_name=fname,last_name=lname,username=name1,email=emal,password=psw1)
        #user = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")
        user.save()
        
        print(name1,psw1)
        return redirect('loanapp:sign')
    
     #   if request.method=='POST':
    elif request.method=='POST' and 'Login' in request.POST:
        name=request.POST.get('email1')
        psw=request.POST.get('pwd1')
        #print(name,psw)
       # return redirect('loanapp:sign')
        user=authenticate(username=name,password=psw)
        if user is not None:
            
            login(request,user)
            return redirect('loanapp:pre')
           
        else:
            messss="Enter correct username or password . Or create new account"

            #return HttpResponse("not correct")
            
    return render(request, 'practice.html',{'messs' : messss})
        
    
def pre(request):
    #{% url 'loanapp:pre' %}
    #if request.method=='GET':
       # return redirect('loanapp:user')
    
    return render(request,'main.html')
def Uuser(request):
    Gender = request.GET['Gender']
    Married = request.GET['Married']
    Dependents = request.GET['Dependents']
    Education = request.GET['Education']
    Self_Employed = request.GET['Self_Employed']
    ApplicantIncome = request.GET['ApplicantIncome']
    CoapplicantIncome = request.GET['CoApplicantIncome']
    LoanAmount = request.GET['LoanAmount']
    Loan_Amount_Term = request.GET['Loan_Amount_Term']
    Credit_History = request.GET['Credit_History']
    Property_Area = request.GET['Property_Area']
    if Gender=="Male":
        Gender=1
    else:
        Gender=0
    if Married =="Yes":
        Married=1
    else:
        Married=0
    if Dependents=="Yes":
        Dependents=1
    else:
        Dependents=0
    if Education=="Graduate":
        Education=1
    else:
        Education=0
    if Self_Employed=="Yes":
        Self_Employed=1
    else:
        Self_Employed=0
    if Credit_History=="More to Pay":
        Credit_History=1
    else:
        Credit_History=0
    if Property_Area=="Urban":
        Property_Area=1
    else:
        Property_Area=0
    Y_predict = model.predict([[Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]])
    if Y_predict[0] == 0:
        Y_predict =" Mostly not Approve"
    else:
        Y_predict ="Mostly Approve"

    
    return render(request,'user.html',{'user' : Y_predict})
def fort(request):
    if request.method=="POST":
        username1=request.POST.get("username")
        psw3=request.POST.get("psw")
        print("ppppp")
        user1 =authenticate(request, username=username1)
        if user1 is not None:
            print("user1")
            u = User.objects.get(username=username1)
            u.set_password(psw3)
            u.save()
        return redirect('loanapp:sign')

    return render(request,'forget.html')
def forg(request):
    messag = None
    if request.method == "POST":
        username = request.POST.get("username")
        new_password = request.POST.get("psw")

        # Authenticate user to ensure the username exists
        try:
        
            user = User.objects.get(username=username)
            # Set the new password and save the user
            user.set_password(new_password)
            user.save()
            messag="Your password has been changed successfully."
            #messages.success(request, "Your password has been changed successfully.")
            #return redirect('loanapp:sign')  # Redirect after success
        except User.DoesNotExist:
            #messages.error(request, "Username does not exist.")
            messag="Username does not exist."
            #return redirect('loanapp:forget')  # Redirect on error

    return render(request, 'forget.html',{'messag' : messag})