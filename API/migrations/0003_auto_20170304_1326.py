# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-04 19:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_auto_20170304_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='name',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
