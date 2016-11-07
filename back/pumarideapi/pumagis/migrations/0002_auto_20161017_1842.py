# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-17 18:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pumagis', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='point',
            options={'verbose_name': 'Point'},
        ),
        migrations.AlterField(
            model_name='point',
            name='lat',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='point',
            name='lon',
            field=models.FloatField(default=0.0),
        ),
    ]
