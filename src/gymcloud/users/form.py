from django.contrib.auth.forms import UserCreationForm
from django import forms
from . import models


class RegisterUser(UserCreationForm):
    username = forms.CharField(label='your_username', max_length=20)
    first_name = forms.CharField(label='your_firstname', max_length=100)
    second_name = forms.CharField(label='your_secondname', max_length=100)
    age = forms.IntegerField(label='your_age')
    email = forms.EmailField(label='your_email')
    password = forms.CharField(label='your_password', max_length=32, widget=forms.PasswordInput)
    
    class Meta:
        model = models.user
        fields = ['username', 'first_name','second_name','age', 'email', 'password', 'password1', 'password2']