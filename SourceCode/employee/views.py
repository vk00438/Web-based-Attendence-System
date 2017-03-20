from django.views import generic
from .models import *
from getdata.models import EmployeeMinutes
from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.utils.html import escape
from django.contrib import auth
from python_arptable import get_arp_table

allemployee=Employee.objects.all()
def index(request):
    return render(request, 'employee/index.html', {})

def about(request):
    return render(request, 'employee/about.html', {})

def dashboard(request):
    empmin = EmployeeMinutes.objects.all()
    for i in empmin:
        i.eid_id = int(i.eid_id)
    return render(request, 'employee/dashboard.html', {'allemp':allemployee, 'empmin':empmin})

def settings(request):
    return render(request, 'employee/settings.html', {})

def ajax(request):
    response_data={}
    gdata=[]
    gdata.append(["Employee","Minutes"])
    for emp in allemployee:
        emptime = EmployeeMinutes.objects.filter(eid=emp.id).order_by('-date')
        for etime in emptime:
            datagraph = []
            datagraph.append(emp.name+' on '+str(etime.date))
            datagraph.append(etime.minutes)
            gdata.append(datagraph)
    response_data["data"]=gdata
    return JsonResponse(response_data)

def showip(request):
    HWaddress=""
    arptable = get_arp_table()
    for row in arptable:
        if row['IP address']==request.META['REMOTE_ADDR']:
            HWaddress=row['HW address']
            break
    return HttpResponse("your Hardware address is %s;" % (HWaddress))