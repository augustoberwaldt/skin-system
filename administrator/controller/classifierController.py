from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from administrator.formsModel import FormDisease
from administrator.model import Disease
from administrator.service import Watson
from django.conf import settings

def index(request):
    list_diseases = Disease.Disease.objects.all()
    paginator = Paginator(list_diseases, 25)
    page = request.GET.get('page')

    try:
        diseases = paginator.page(page)
    except PageNotAnInteger:
        diseases = paginator.page(1)
    except EmptyPage:
        diseases = paginator.page(paginator.num_pages)

    return render(request, 'classifier/index.html', {'diseases': diseases})

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

            createClassifirWatson(namefile)
            form.save()

    return render(request,'classifier/add_edit.html',{})


def createClassifirWatson(name):
   watson = Watson.Watson()
   watson.createClassifier(name)