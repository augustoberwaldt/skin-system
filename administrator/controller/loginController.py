from django.shortcuts import render, redirect
from django.contrib.auth import  authenticate, login, logout
from administrator.formsModel import FormUser
from django.contrib.auth.hashers import make_password

def do_login(request):

    if request.method  == 'POST' :
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None :
            login(request,user)
            return redirect('/admin/home')

    return render(request, 'auth/login.html')

def resetPass(request):
    return render(request, 'auth/resetPassword.html')

def register(request):

    form = FormUser.FormUser(request.POST or None);
    context = {'form': form}

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/admin/register')

    return render(request, 'auth/register.html', context)


def do_logout(request):
    logout(request)
    return redirect('/admin/')


