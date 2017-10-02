from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from administrator.formsModel import FormDisease
from administrator.model import Disease
from administrator.service import Watson , Upload
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import json

@login_required
def index(request):

    list_diseases = Disease.Disease.objects.all()
    paginator = Paginator(list_diseases, 5)
    page = request.GET.get('page')

    try:
        diseases = paginator.page(page)
    except PageNotAnInteger:
        diseases = paginator.page(1)
    except EmptyPage:
        diseases = paginator.page(paginator.num_pages)

    return render(request, 'classifier/index.html', {'diseases': diseases})

@login_required
def add(request):

    if request.method == "POST":
        form = FormDisease.FormDisease(request.POST)
        if form.is_valid():
            filePositive = request.FILES['filePositive']
            fileNegative = request.FILES['fileNegative']

            fs = FileSystemStorage()
            namefile = request.POST['name'] +'_'+ request.POST['type'] + '';
            filenameP = fs.save(namefile +'_positive', filePositive)
            filenameN = fs.save(namefile +'_negative', fileNegative)
            uploaded_file_url = fs.url(filenameP)
            uploaded_file_url = fs.url(filenameN)

            ret = createClassifirWatson(namefile)
            form.setClassfierId(ret['classifier_id'])
            form.save()

    return render(request, 'classifier/add_edit.html',{})


def createClassifirWatson(name):
    watson = Watson.Watson()
    return watson.createClassifier(name)


@login_required
def getDisease(request):
    file = request.FILES['fileUpload']
    fs = FileSystemStorage()
    fs.save(file.name, file)
    up = Upload.Upload()
    up.setDir("skin-system")
    uploaded = up.process(file.name)

    watson = Watson.Watson()
    response = watson.classifier(uploaded.get('url'));
    parse = Watson.Parser();
    return HttpResponse(parse.parseResponseClassifier(response), content_type="application/json")

@login_required
def removeClassifier(request):
    watson = Watson.Watson()

    try:
        disease = Disease.Disease.objects.get(pk=request.GET['id'])
        watson.deleteClassifier(disease.classifier_id)
        reponse = {'title': 'Registro deletado !', 'message': '', 'type': 'success'}
        messages.add_message(request, messages.SUCCESS, json.dumps(reponse))
    except Exception :
        reponse = {'title': 'ops ocorreu um erro', 'message': '', 'type': 'error'}
        messages.add_message(request, messages.ERROR, json.dumps(reponse))

    return redirect('/app/classifier')


@login_required
def getAllClassfiers(request):
    watson = Watson.Watson()
    return HttpResponse(watson.listClassifiers(), content_type="application/json")