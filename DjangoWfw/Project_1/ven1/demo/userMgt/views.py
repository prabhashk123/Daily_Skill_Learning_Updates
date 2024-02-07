from django.shortcuts import render
from userMgt.forms import CustomerForm
from django.contrib.auth.forms import UserCreationForm
from django.http.response import HttpResponse
# user autneticate login and logout import
from django.contrib.auth import authenticate,login,logout
#secure authticate use decorators
from django.contrib.auth.decorators import login_required
# decorator import
from .decorators import login_not_required 

# Create your views here.
@login_not_required
def view_sign_up(request):
    if request.method=="GET":
        frm_user=UserCreationForm()
        frm_cus=CustomerForm()
        d1={'frm_user':frm_user,'frm_cus':frm_cus}
        return render(request,'userMgt/signup.html',context=d1)
    elif request.method=="POST":
        frm_user=UserCreationForm(request.POST)
        frm_cus=CustomerForm(request.POST)
        d1={'frm_user':frm_user,'frm_cus':frm_cus}
        if(frm_user.is_valid() and frm_cus.is_valid()):
            # for secure
            u=frm_user.save()
            # we can write the code here we want to do before insert User
            # is_staff on karna hai to
            # u=frm_user.save(commit=False)
            # u.is_staff=True
            # u.save()
            # we can write the code here we want to do aftrer insert User
            # here commit means not data save in database
            c=frm_cus.save(commit=False)
            c.user=u
            c.save()
            return HttpResponse("Customer created successfully")
        else:
            return render(request,'userMgt/signup.html',context=d1)
        
def view_home(request):
    return render(request,'userMgt/home.html')
# without login secure page pe nhi ja sakte hai
@login_required(login_url='login')
def view_secure1(request): 
    return render(request,'userMgt/secure1.html')
def view_secure2(request):
    return render(request,'userMgt/secure2.html')
def view_unsecure1(request):
    return render(request,'userMgt/unsecure1.html')
def view_unsecure2(request):
    return render(request,'userMgt/unsecure2.html')
@login_not_required
def view_login(request):
    if(request.method=='GET'):
        return render(request,'userMgt/login.html')
    elif(request.method=='POST'):
        # first read request.post then write
        username=request.POST.get('username')
        password=request.POST.get('password')
        u=authenticate(request,username=username,password=password)
        if u is not None:
            # login at system then login method 
            login(request,u)
            return render(request,'userMgt/login.html')
        else:
            d1={'msg':'UserName or Password Incorrect'}
            return render(request,'userMgt/login.html',context=d1)
# For logout
def view_logout(request):
    if(request.user.is_authenticated):
        logout(request)
    return render(request,'userMgt/home.html')


