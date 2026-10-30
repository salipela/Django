from django.shortcuts import render,redirect,get_object_or_404
from myapp.forms import StudentForm
from myapp.models import Student
def home(request):
    return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about.html')

def  register(request):
   form = StudentForm()
   if request.method == 'POST':
       form = StudentForm(request.POST)
       if form.is_valid():
           form.save(commit=True)
           return redirect('students')
   return render(request, 'myapp/register.html', {'form': form})

def contact(request):
    return render(request, 'myapp/contact.html')

def delete(request,id):
    stu=get_object_or_404(Student,StudentId=id)
    if request.method=='POST':
        stu.delete()
        return redirect('students')

    return render(request, 'myapp/delete.html',{'student':stu})
    

def details(request,id):
    stu=get_object_or_404(Student,StudentId=id)
    return render(request, 'myapp/details.html', {'student':stu})
    


def students(request):
    studs = Student.objects.all()
    return render(request, 'myapp/students.html', {'stu_list': studs})




def edit(request, id):
    stu = get_object_or_404(Student, StudentId=id)
    form = StudentForm(instance=stu)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=stu)
        if form.is_valid():
            form.save()
            return redirect('students')

    return render(request, 'myapp/edit.html', {'form': form})


