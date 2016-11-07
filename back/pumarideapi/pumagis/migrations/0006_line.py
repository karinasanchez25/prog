# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-17 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pumagis', '0005_remove_point_shortest_path'),
    ]

    operations = [
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('p_origen', models.CharField(default=b'(0,0)', max_length=50)),
                ('p_destino', models.CharField(default=b'(0,0)', max_length=50)),
                ('shortest_path', models.CharField(default=b'', max_length=5000)),
            ],
            options={
                'verbose_name': 'Point',
            },
        ),
    ]
