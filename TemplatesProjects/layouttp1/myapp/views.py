from django.shortcuts import render


def home(request):
    return render(request, 'myapp/home.html')


def about(request):
    return render(request, 'myapp/home.html')


def register(request):

    employees = [
        {
            "id": 101,
            "name": "Sushmitha",
            "job": "Developer"
        },
        {
            "id": 102,
            "name": "Varsha",
            "job": "Tester"
        },
        {
            "id": 103,
            "name": "Shivani",
            "job": "Designer"
        },
        {
            "id": 104,
            "name": "Manasvi",
            "job": "HR"
        },
        {
            "id": 105,
            "name": "Rahul",
            "job": "Manager"
        },
        {
            "id": 106,
            "name": "Priya",
            "job": "Developer"
        },
        {
            "id": 107,
            "name": "Arjun",
            "job": "Tester"
        },
        {
            "id": 108,
            "name": "Sneha",
            "job": "Analyst"
        },
        {
            "id": 109,
            "name": "Kiran",
            "job": "Designer"
        },
        {
            "id": 110,
            "name": "Divya",
            "job": "Developer"
        }
    ]

    student = [
        {
            "name": "poojitha",
            "age": 24,
            "marks": 95
        },
        {
            "name": "vamsi",
            "age": 23,
            "marks": 97
        },
        {
            "name": "pooji",
            "age": 20,
            "marks": 93
        }
    ]

    context = {
        'emplist': employees,
        'stulist': student
    }

    return render(request, 'myapp/register.html', context)


def login(request):
    return render(request, 'myapp/login.html')