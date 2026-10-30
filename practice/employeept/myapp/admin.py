from django.contrib import admin
from .models import employee
class employeeAdmin(admin.ModelAdmin):
    list_display = ('employeeId', 'employeeName', 'employeeAge')
    class Meta:
        model = employee

admin.site.register(employee, employeeAdmin)

# Register your models here.
