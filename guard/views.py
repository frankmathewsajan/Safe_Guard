from django.shortcuts import render


def welcome(request):
    return render(request, 'guard/welcome.html')


def login(request):
    return render(request, 'guard/auth/login.html')


def register(request):
    return render(request, 'guard/auth/register.html')


def tracking(request):
    return render(request, 'guard/tracking.html',{
        "details": {
            "longitude": 6.5244,
            "latitude": 3.3792,
            "address": "Lagos, Nigeria",
            "time": "12:00 PM",
            "date": "12/12/2020"
        }
    })


def home(request):
    return render(request, 'guard/home.html')


def features(request):
    return render(request, 'guard/features.html')


def dashboard(request):
    return render(request, 'guard/dashboard.html')
