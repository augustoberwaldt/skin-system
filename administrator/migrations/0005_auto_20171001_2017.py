# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-01 20:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0004_auto_20170903_0111'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease',
            name='classifier_id',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='disease',
            name='description',
            field=models.TextField(max_length=150),
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
