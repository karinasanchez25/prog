# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-03 03:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pumagis', '0012_line__shortest_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='line',
            name='_shortest_path',
        ),
    ]
