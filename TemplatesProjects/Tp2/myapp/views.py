from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')
def register(request):
    return render(request, 'myapp/register.html')
def login(request):
    return render(request, 'myapp/login.html')
def info(request):
    return render(request, 'myapp/info.html')