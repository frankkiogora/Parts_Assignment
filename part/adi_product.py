import requests
import json
import csv

api_key = '8c0bb92a'

url = 'https://octopart.com/api/v3/parts/search?apikey=8c0bb92a&q=AD9361*&pretty_print=true'
r = requests.get(url).json()
# print '*******  RESULTS_LENGTH ********  ', len(r['results'])
# print '*******  FIRST_RESULT  ********  ', r['results'][0]
# print '*******  FIRST_RESULT_RESULT_KEYS  ********  ', r['results'][0].keys()# snippet, item , class
# print '*******  FIRST_RESULT_ITEM  ********  ', r['results'][0]['item']

c = csv.writer(open('mytemps.csv', 'w'))
columns = ['Distributor', 'mpn', 'Pins', 'Price', 'Frequency']
c.writerow(columns)


for result in r['results']:
    manufacturer = result['item']['manufacturer']['name']
    mpn = result['item']['mpn']
    # item one
    item_one_pins = r['results'][0]['snippet'].split()[3]
    c.writerow([manufacturer, mpn, item_one_pins, 'price', 'unavailable'])

# item one
mpn = mpn

# item two
item_two_pins = r['results'][1]['snippet'].split()[3]
c.writerow([manufacturer, mpn, item_two_pins, 'Price', 'unavailable'])

# item three

item_three_pins = 'none'
c.writerow([manufacturer, mpn, item_three_pins,
            'unavailable', 'unavailable'])

# item four

item_four_pins = 'none'
c.writerow([manufacturer, mpn, item_four_pins, 'unavailable', 'Frequency'])

# currency and dollar_amount extraction


for result in r['results']:
    offers = result['item']['offers']
    for offer in offers:
        for k, v in offer['prices'].iteritems():
            currency = k
            # print '****  currency  ****', currency
            dollar_amount = float(v[0][1])
        currency = k
        # print currency
        dollar_amount = dollar_amount
        # print dollar_amount
