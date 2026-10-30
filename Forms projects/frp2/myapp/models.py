from django.db import models

class Student(models.Model):
    StudentId = models.CharField(primary_key=True)
    StudentName = models.CharField(max_length=100)
    StudentMarks = models.IntegerField()

# Create your models here.
