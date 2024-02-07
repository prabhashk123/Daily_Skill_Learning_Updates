from django.shortcuts import render

# Create your views here.
def view_home(request):
    return render(request,'dtl/home.html')

def view_variable(request):
    d1={'var1':'Welcome To DTL','var2':'Django'}
    return render(request,'dtl/variable_ex.html',context=d1)
def view_base(request):
    return render(request,'dtl/base.html')
def view_homes(request):
    return render(request,'dtl/homes.html')
def view_ifexample(request):
    list1=['Prabhash','Subhash']
    d1={'list1':list1,'var':'<>34',}
    return render(request,'dtl/ifexample.html',context=d1)

"""print all students from database from model"""
from newappdbms.models import Student
def view_fatch_all_stu(request):
    allstu=Student.objects.all()
    d1={'allstu':allstu}
    return render(request,'dtl/fatch_all_stu.html',context=d1)

"""for session"""
def view_writesession(request):
    if request.method=='POST':
        request.session['mydata']=request.POST.get('textdata')
        request.session.set_expiry(30)
        # for cookies
    resp=render(request,'dtl/writesession.html')
    resp.set_cookie('mycookies','my data for cookies',max_age=30)
    return resp

def view_readsession(request):
    cookies_data=request.COOKIES.get("myccokies",'Cookies Expired')
    d1={'data':cookies_data}
    return render(request,'dtl/readsession.html',context=d1)

