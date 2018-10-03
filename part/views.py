# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
import requests
from part.models import Part


def parts_search(request):
    snippet = ''
    url = 'https://octopart.com/api/v3/parts/search?apikey=8c0bb92a&q=AD9361*&pretty_print=true'
    r = requests.get(url)
    json_object = r.json()
    results = json_object['results']

    for result in results:
        snippet = result['snippet']
        offers = result['item']['offers']
    for offer in offers:
        distributor = offer['seller']['name']
        sku = offer['sku']
        moq = offer['moq']
        leads = offer['factory_lead_days']
        stock = offer['in_stock_quantity']
        pkg = offer['packaging']
        prices = offer['prices']

        for price in prices:
            price = price[1]
    print 'snippet', snippet
    return redirect('/parts')


def index(request):
    return render(request, "parts_app/index.html")


def parts(request):
    context = {
        'parts': Part.objects.all()
    }
    return render(request, "parts_app/parts.html", context)
