# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Part(models.Model):
    distributor_name = models.CharField(max_length=255, default="")
    sku = models.CharField(max_length=255)
    moq = models.CharField(max_length=255)
    snippet = models.CharField(max_length=255)
    leads = models.CharField(max_length=255)
    stock = models.CharField(max_length=255)
    pkg = models.CharField(max_length=255, default="Tray")
    prices = models.CharField(max_length=255, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.distributor_name
