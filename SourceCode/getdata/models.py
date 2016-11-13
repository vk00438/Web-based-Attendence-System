from __future__ import unicode_literals

from datetime import date
from django.db import models
from employee.models import Employee


class EmployeeMinutes(models.Model):
    class Meta:
        unique_together = ("date", "eid")

    date = models.DateField(default=date.today)
    eid = models.ForeignKey(Employee, on_delete=models.CASCADE)
    minutes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.eid_id)+' / '+str(self.date)
