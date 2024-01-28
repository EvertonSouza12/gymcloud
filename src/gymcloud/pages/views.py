from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def workouts(request):
    return render(request, 'workouts.html')

def manage_workout(request):
    return render(request, 'manage_workout.html')

def manage_customers(request):
    return render(request, 'manage_customers.html')