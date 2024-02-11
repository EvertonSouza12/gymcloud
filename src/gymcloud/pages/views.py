from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def setings(request):
    return render(request, 'setings.html')

def manage_workouts(request):
    return render(request, 'manage_workouts.html')

def workouts(request):
    return render(request, 'workouts.html')