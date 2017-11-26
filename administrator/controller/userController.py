from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from administrator.formsModel import FormUser
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
import json

@login_required
def index(request):
    users = User.objects.all()
    paginator = Paginator(users, 5)
    page = request.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'user/index.html', {"users" : users})



@login_required
def password_change(request):
  
    if request.method == 'POST' and request.POST['password'] == request.POST['reppassword']:
        
        u = User.objects.get(username=request.user)  
        u.set_password(request.POST['password'])
        u.save()
        update_session_auth_hash(request, u)
        reponse = {'title': 'Success ', 'message': 'Atualiazado com sucesso !', 'type': 'success'}
        messages.add_message(request, messages.INFO, json.dumps(reponse))
        return redirect('account')
    else:
        reponse = {'title' : 'Dados invalidos ! ', 'message' : 'Tente novamente.', 'type' : 'error' }

        messages.add_message(request, messages.INFO, json.dumps(reponse)) 

    
    return render(request, 'account/index.html', {}) 