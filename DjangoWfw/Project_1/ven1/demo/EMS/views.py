from django.shortcuts import render
from .forms import EmployeeForm
from .models import Employees
from django.http.response import HttpResponse

# Create your views here.
def employeeform(request):
    if request.method=='GET':
        empform=EmployeeForm()
        d1={'empform':empform}
        return render(request,'EMS/employee.html',context=d1)
    elif request.method=='POST':
        empform=EmployeeForm(request.POST)
        d1={'empform':empform}
        if (empform.is_valid):
            empform.save()
            return HttpResponse("Employee Details Added Succesfully")    
        else:
            return render(request,'EMS/employee.html',context=d1)
def employeeform(request):
    d1={}
    if(request.method=='POST'):
        emp=Employees()
        emp.Emp_id=request.POST.get('Emp_id')
        emp.Emp_name=request.POST.get('Emp_name')
        emp.Emp_mobno=request.POST.get('Emp_mobno')
        emp.Emp_age=request.POST.get('Emp_age')
        emp.Emp_depart=request.POST.get('Emp_depart')
        emp.Emp_depart=request.POST.get('Emp_depart')
        emp.Emp_role=request.POST.get('Emp_role')
        emp.Emp_expinyears=request.POST.get('Emp_expinyears')
        emp.save()
        return HttpResponse('Employee Added Successfully')
    allemp=Employees.objects.all()
    d1['allemp']=allemp
    return render(request,'EMS/employee.html',context=d1)

def emsform(r):
    return render(r,'EMS/emsform.html')
