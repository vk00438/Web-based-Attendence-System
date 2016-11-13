from django.views import generic
from .models import *
from getdata.models import *
from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth



def index(request):
    return render(request, 'employee/index.html', {})

def about(request):
    return render(request, 'employee/about.html', {})

def dashboard(request):
    allemployee=Employee.objects.all()
    emp_min=EmployeeMinutes.objects.all()
    for i in emp_min:
        i.eid_id=int(i.eid_id)

    return render(request, 'employee/dashboard.html', {'allemp':allemployee, 'empmin':emp_min})

def settings(request):
    return render(request, 'employee/settings.html', {})