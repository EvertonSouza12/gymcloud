from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password

class register(forms.Form):
    first_name = forms.CharField(label='Your name', max_length=100)
    second_name = forms.CharField(label='Your name', max_length=100)
    age = forms.IntegerField(label='Your age', max_value=110)
    email = forms.EmailInput(label='Your e-mail')
    password = forms.CharField(label='Your password', max_length=32, widget=forms.PasswordInput)
    
    
def register_user(request):
    if request.method == 'POST':
        form = register(request.POST)
        if form.is_valid():
            register.password = make_password(register.password)
            return HttpResponseRedirect('/thanks')
    else:
        form = register()
    return render (request, 'register.html')