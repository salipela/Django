from django.shortcuts import render

from django.http import HttpResponse

# fbv  functon based view bcz where we are using function based view we have to create a function and pass the request as a parameter and return the response in the form of HttpResponse.
def home(request):
    return HttpResponse("<h1 style='text-align: center;color:blue;'>Welcome to the Home Page!</h1>")

def register(request):
    return HttpResponse("<h1 style='text-align: center;color:green;'>This is the Register Page!</h1>")
def login(request):
    return HttpResponse("<h1 style='text-align: center;color:orange;'>This is the Login Page!</h1>")
def about(request):
    return HttpResponse("<h1 style='text-align: center;color:purple;'>This is the About Page!</h1>")
def contact(request):
    return HttpResponse("<h1 style='text-align: center;color:red;'>This is the Contact Page!</h1>")
