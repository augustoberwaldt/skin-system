

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'classifier/index.html', {'diseases': [{}, {}, {}, {}]})

def add(request):
    return render(request,'classifier/add_edit.html',{})
