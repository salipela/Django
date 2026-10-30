from django.contrib import admin
from .models import Student
class StudentAdmin(admin.ModelAdmin):
    list_display = ('StudentId', 'StudentName', 'StudentMarks')
    class Meta:
        model = Student

admin.site.register(Student, StudentAdmin)

# Register your models here.
