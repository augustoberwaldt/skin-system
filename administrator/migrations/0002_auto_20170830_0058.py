# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-30 00:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disease',
            name='description',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='disease',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='disease',
            name='type',
            field=models.CharField(max_length=150),
        ),
    ]
