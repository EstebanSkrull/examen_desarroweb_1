# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 02:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
