from django.shortcuts import render,redirect,get_object_or_404
from myapp.forms import employeeForm
from myapp.models import employee
def home(request):
    return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about.html')

def  register(request):
   form = employeeForm()
   if request.method == 'POST':
       form = employeeForm(request.POST)
       if form.is_valid():
           form.save(commit=True)
           return redirect('employee')
   return render(request, 'myapp/register.html', {'form': form})

def contact(request):
    return render(request, 'myapp/contact.html')

def delete(request,id):
    employee=get_object_or_404(employee,employeeId=id)
    if request.method=='POST':
        employee.delete()
        return redirect('employee')

    return render(request, 'myapp/delete.html',{'employee':employee})
    

def details(request,id):
    employee=get_object_or_404(employee,employeeId=id)
    return render(request, 'myapp/details.html', {'employee':employee})
    


def employee(request):
    employee = employee.objects.all()
    return render(request, 'myapp/employee.html', {'emp_list': employee})




def edit(request, id):
    employee = get_object_or_404(employee, employeeId=id)
    form = employeeForm(instance=employee)

    if request.method == 'POST':
        form = employeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee')

    return render(request, 'myapp/edit.html', {'form': form})


