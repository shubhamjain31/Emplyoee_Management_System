from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.models import User ,auth
from django.contrib.auth.decorators import login_required

from App.forms import CompanyForm, EmployeeForm
from App.models import *

# Create your views here.

@login_required(login_url='login')
def home(request):
    return render(request,'home.html')

@login_required(login_url='login')
def add_company(request):
    if request.method == "POST":

        form = CompanyForm(request.POST)
        if form.is_valid():
            post        = form.save(commit=False)
            post.user   = request.user

            try:
                post.save()
                messages.success(request, 'Company Added Successfully !')
                return redirect("/show")
            except Exception as e:
                print(e)
    else:
        form = CompanyForm()
    return render(request, "index.html", {'form':form})

@login_required(login_url='login')
def show_company(request):
    companies   = Company.objects.all()

    return render(request, "showcompany.html", {'companies':companies})

@login_required(login_url='login')
def add_employee(request):
    last = request.META.get('HTTP_REFERER', None)

    if request.method == "POST":

        form = EmployeeForm(request.POST)
        if form.is_valid():
            post        = form.save(commit=False)

            try:
                post.save()
                messages.success(request, 'Employee Added Successfully !')
                return redirect(last)
            except Exception as e:
                print(e)
    else:
        form = EmployeeForm()
    return render(request, "employee/addemployee.html", {'form':form})

@login_required(login_url='login')
def show_employee(request):
    employees   = Employee.objects.all()

    return render(request, "employee/showemployee.html", {'employees':employees})