from django import forms
from .models import Student
class StudentForm(forms.ModelForm):
    StudentId = forms.CharField()
    StudentName = forms.CharField(max_length=40)
    StudentMarks = forms.IntegerField()
    class Meta:
        model = Student
        fields ='__all__'

