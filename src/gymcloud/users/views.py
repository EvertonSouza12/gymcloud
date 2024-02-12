from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import UserCreationForm
from .models import user

class register(UserCreationForm):
    username = forms.CharField(label='Your username', max_length=20)
    first_name = forms.CharField(label='Your name', max_length=100)
    second_name = forms.CharField(label='Your name', max_length=100)
    age = forms.IntegerField(label='Your age')
    email = forms.EmailInput(label='Your e-mail')
    password = forms.CharField(label='Your password', max_length=32, widget=forms.PasswordInput)
    
    class RegisterForm(UserCreationForm):
    
        class Meta:
            model = user
            fields = ['first_name','second_name','age', 'email', 'password']
    
    
def register_user(request):
    if request.method == 'POST':
        form = register(request.POST)
        if form.is_valid():
            register.password = make_password(register.password)
            return HttpResponseRedirect('')
    else:
        form = register()
    return render (request, 'register.html')