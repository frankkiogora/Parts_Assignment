# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-01 21:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0002_part_pkg'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='prices',
            field=models.CharField(default='', max_length=255),
        ),
    ]
