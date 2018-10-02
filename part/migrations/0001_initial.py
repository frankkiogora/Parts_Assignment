# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-01 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distributor_name', models.CharField(default='', max_length=255)),
                ('sku', models.CharField(max_length=255)),
                ('moq', models.CharField(max_length=255)),
                ('snippet', models.CharField(max_length=255)),
                ('leads', models.CharField(max_length=255)),
                ('stock', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
