from django import forms
from .models import employee
class employeeForm(forms.ModelForm):
    employeeId = forms.CharField()
    employeeName = forms.CharField(max_length=40)
    employeeAge = forms.IntegerField()
    class Meta:
        model = employee
        fields ='__all__'

