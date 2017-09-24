from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


@login_required
def index(request):
    users = User.objects.all()
    return render(request, 'user/index.html', {"users" : users})