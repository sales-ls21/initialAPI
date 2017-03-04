# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-04 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appuser',
            name='user',
        ),
        migrations.AddField(
            model_name='appuser',
            name='first_name',
            field=models.CharField(default=None, max_length=60),
        ),
        migrations.AddField(
            model_name='appuser',
            name='last_name',
            field=models.CharField(default=None, max_length=60),
        ),
    ]
