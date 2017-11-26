from django.shortcuts import render, redirect
from django.contrib.auth import  authenticate, login, logout
from administrator.formsModel import FormUser
from django.contrib import messages
import json

def do_login(request):

    if request.method  == 'POST' :
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None :
            login(request,user)
            return redirect('/app/home')
        else :
            reponse = {'title' : 'Dados invalidos ! ', 'message' : 'Tente novamente.', 'type' : 'error' }

            messages.add_message(request, messages.INFO, json.dumps(reponse))

    if request.user.is_authenticated():
        return redirect('/app/home')
    
    return render(request, 'auth/login.html')

def resetPass(request):
    return render(request, 'auth/resetPassword.html')

def register(request):

    form = FormUser.FormUser(request.POST or None);
    context = {'form': form}

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            reponse = {'title': 'Success ', 'message': 'Cadastro realizado !', 'type': 'success'}
            messages.add_message(request, messages.INFO, json.dumps(reponse))
            return redirect('/app/register')
        else :
            reponse = {'title': 'Dados invalidos ! ', 'message': 'Tente novamente.', 'type': 'error'}
            messages.add_message(request, messages.INFO, json.dumps(reponse))

    return render(request, 'auth/register.html', context)


def do_logout(request):
    logout(request)
    reponse = {'title': 'Success ', 'message': 'Saida com sucesso !', 'type': 'success'}
    messages.add_message(request, messages.INFO, json.dumps(reponse))
    return redirect('/app/')


