from django.db import models

class employee(models.Model):
    employeeId = models.CharField(primary_key=True)
    employeeName = models.CharField(max_length=100)
    employeeMarks = models.IntegerField()

# Create your models here.
