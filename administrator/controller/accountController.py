from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url="/admin")
def index(request):
    return render(request, 'account/index.html', {'diseases': [{}, {}, {}, {}]})