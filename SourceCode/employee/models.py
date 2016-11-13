from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=250)
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('employee:settings',kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.id) + '-' + self.name

class EmployeeMac(models.Model):
    eid = models.ForeignKey(Employee, on_delete=models.CASCADE)
    mac_address = models.CharField(max_length=17)
    def __str__(self):
        return str(self.eid_id) + '-' + self.mac_address

