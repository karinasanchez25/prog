# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-17 19:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pumagis', '0004_point_shortest_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='point',
            name='shortest_path',
        ),
    ]