#!/usr/bin/python
import subprocess, time, django, sys, os

sys.path.append(os.path.abspath("/home/kirito/Documents/moniter"))
os.environ['DJANGO_SETTINGS_MODULE'] = 'moniter.settings'
django.setup()

from getdata.models import *
from employee.models import *

# dictionary for mac-address count
mac_time ={}

# def xyz():
# cmd='for ip in $(seq 1 254);do arp 10.42.0.$ip|grep -oh "[a-f0-9][a-f0-9]:[a-f0-9][a-f0-9]:[a-f0-9][a-f0-9]:[a-f0-9][a-f0-9]:[a-f0-9][a-f0-9]:[a-f0-9][a-f0-9] " ;done'
# os.system(cmd)

def count():
    time.sleep(60- (int(time.time()) % 60))
    print("entering time",time.time())
    #change your IP here
    ip='10.42.0.'
    cmdfnmap = 'nmap -sn '+ip+'*'
    subprocess.check_output(cmdfnmap, shell=True)
    cmdfmac = 'for ip in $(seq 1 254);do arp '+ip+'$ip|grep -oh "[a-f0-9][a-f0-9]:[a-f0-9][a-f0-9]:[a-f0-9][a-f0-9]:[a-f0-9][a-f0-9]:[a-f0-9][a-f0-9]:[a-f0-9][a-f0-9]" ;done'
    proc = subprocess.Popen(cmdfmac, shell=True, stdout=subprocess.PIPE, )
    output = proc.communicate()[0]
    words = output.split('\n')
    words=[x for x in words if len(x)!=0]
    for i in words:
        mac_time[i]=mac_time.get(i, 0)+1

def printmac():
    print (mac_time)

#fill minutes in range
for i in range(2):
    count()
    printmac()

# mac_time ={'9c:d3:5b:14:45:98': 13, 'b4:6d:83:3a:20:8c': 9}

empmac = EmployeeMac.objects.all()
mac_emp = {ob.mac_address:ob.eid_id for ob in empmac}
emp_time = {}

for mac in mac_time:
    if mac in mac_emp:
        eid=mac_emp[mac]
        emp_time[eid]=max(emp_time.get(eid,0),mac_time[mac])


for i in emp_time:
    etobject = EmployeeMinutes()
    print(i)
    etobject.eid_id=i
    etobject.minutes=emp_time[i]
    etobject.save()


print("database updated")



