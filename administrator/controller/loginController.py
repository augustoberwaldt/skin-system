
from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'auth/login.html')

def resetPass(request):
    return render(request, 'auth/resetPassword.html')

def register(request):
    return render(request, 'auth/register.html')

def register(request):
    return render(request, 'auth/register.html')



def logout(request):
    return redirect('/admin/')


