from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, "index.html")

# Create your views here.
def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, "all_emp.html")

# Create your views here.
def add_emp(request):
    if request.method == "POST":
    #     print("POST")
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        rolename = int(request.POST['rolename'])
        deptname = int(request.POST['deptname'])
        deptLocation = int(request.POST['deptLocation'])
        hire_date = int(request.POST['hire_date'])
        new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary, 
                        bonus=bonus, phone=phone, rolename=rolename, deptname=deptname, 
                        deptLocation=deptLocation, hire_date=hire_date)
        new_emp.save()

        return HttpResponse("Employee Added Successfully")

    elif request.method == 'GET':
    #     print('GET')
        return render(request, "add_emp.html")
    
    else:
        return HttpResponse("An exception occured")    

# Create your views here.
def remove_emp(request, emp_id=0):
   if emp_id:
       try:
        emp_to_be_removed = Employee.objects.get(id=emp_id)
        emp_to_be_removed.delete()
        emps = Employee.objects.all()
        context = {
            'emps': emps
        }
        return HttpResponse("Employee Removed Successfully")
       except:
        return HttpResponse("An error encountered")
   return render(request, "remove_emp.html")

# Create your views here.
def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(first_name__icontains = name) | Q(last_name__icontains = name)
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)

        context = {
            'emps': emps
        }
    return render(request, "filter_emp.html")

