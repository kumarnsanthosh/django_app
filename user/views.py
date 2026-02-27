from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import RegisterForm
from .models import Profile
# Create your views here.


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f'logged in as {username}')
            return redirect('myapp:home')
        else:
            messages.error(request, 'login failed')
            return redirect('user:login')
    return render(request, 'login.html')

def logout_page(request):
    if request.method == 'POST':
        logout(request)
        return redirect('myapp:home')



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:login')    
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
        




def view_profile(request):
    profile = Profile.objects.get_or_create(user=request.user)
    return render(request, 'profile.html', {'profile': profile})
    
    
def test(request):
    user = "Profile.objects.get()"
    print(user)
    
    return HttpResponse("Working")