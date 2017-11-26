# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'sobre.html')


def contact(request):
    return render(request, 'contato.html')
