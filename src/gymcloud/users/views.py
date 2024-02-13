from django.shortcuts import render, redirect
from .form import RegisterUser
from django.contrib import messages



def register(request):
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada')
            return redirect('gymcloud-home', {'form':form})
    else:
        form = RegisterUser()
    return render(request, 'register.html', {'form':form})


def login(request):
    return render(request, 'login.html')