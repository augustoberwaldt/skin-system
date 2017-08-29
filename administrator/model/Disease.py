from django.db import models

class Disease(models.Model) :
    name = models.CharField(max_length=80)
    type = models.CharField(max_length=80)
    description = models.CharField(max_length=200)