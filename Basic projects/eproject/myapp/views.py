from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1 style='text-align: center;color:blue;'>Welcome to the Home Page!</h1>")

def register(request):
    return HttpResponse("<h1 style='text-align: center;color:green;'>This is the Register Page!</h1>")
def login(request):
    return HttpResponse("<h1 style='text-align: center;color:orange;'>This is the Login Page!</h1>")
def about(request):
    return HttpResponse("<h1 style='text-align: center;color:purple;'>This is the About Page!</h1>")
def contact(request):
    return HttpResponse("<h1 style='text-align: center;color:purple;'>This is the Contact Page!</h1>")