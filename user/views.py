from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f'{username} logged in')
            return redirect('myapp:home')
        else:
            messages.error(request, 'login failed')
            return redirect('user:login')
    return render(request, 'login.html')