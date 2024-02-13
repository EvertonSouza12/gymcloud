from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
            
def home(request):
    return render(request,'home.html')

def setings(request):
    return render(request, 'setings.html')

def manage_workouts(request):
    return render(request, 'manage_workouts.html')

def workouts(request):
    return render(request, 'workouts.html')