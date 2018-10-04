import requests
import json
import csv


api_key = '8c0bb92a'

url = 'https://octopart.com/api/v3/parts/search?apikey=8c0bb92a&q=AD9361*&include[]=specs&sort=specs2.15.numbers&sort-dir=asc&start=0&pretty_print=true'
r = requests.get(url).json()

results = r['results']
item_one_manufacturer = results[0]['item']['manufacturer']['name']

# csv file setup

c = csv.writer(open('mytemps.csv', 'w'))

# ==========    Headers   ===============

c.writerow(['MANUFACTURER', 'SNIPPET', 'MPN',
            'NO.PINS', 'FREQUENCY', 'PACKAGING', 'RANGE'])


for result in results:
    part = result['item']
    manufacturer = part['manufacturer']['name']
    mpn = part['mpn']
    snippet = result['snippet']

    # ==========    item two  ================
    item1 = results[0]['item']

    item1_pin = item1['specs']['pin_count']['display_value']
    item1_freq = item1['specs']['frequency']['display_value']
    item1_pkg = item1['specs']['packaging']['display_value']

    c.writerow([manufacturer, snippet, mpn,
                item1_pin, item1_freq, item1_pkg, ''])

    # ==========    item two  ================
    item2 = results[1]['item']
    item2_pin_count = item2['specs']['pin_count']['display_value']
    item2_pkg = item2['specs']['packaging']['display_value']

    c.writerow([manufacturer, snippet, mpn,
                item2_pin_count, '', item2_pkg, ''])

    # ==========    item three  ================

    c.writerow([manufacturer, snippet, mpn, '', '', '', ''])

    # ==========    item four  ================

    c.writerow([manufacturer, snippet, mpn, '', '', '', ''])


#  ++ private notes ++
# fix the code to avoid printing 4 times. I suspect the reapeting lines has to fo with the url, need more time to analyse and fix
# Study and finish 'one hot encoding
