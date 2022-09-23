#!/usr/bin/env python3
import json

TAX_RATE = 0.3

with open('response.json') as fd:
    results = json.loads(fd.read())

units = {
    '0.5g': ('price_half_gram', 2),
    '1g':('price_gram', 1),
    '2g':('price_two_gram', 0.5),
    '3.5g':('price_eighth_ounce', 0.285714),
    '7g':('price_quarter_ounce', 0.142857),
    '14g':('price_half_ounce', 0.0714285),
    '28g':('price_ounce', 0.03571425)
}

# (price index, dict)
items = list()

def get_price(f):
    return float(x['discounted_'+f] or x[f] or 0)

for x in results['hits']:
    if 'flower' in x['root_types']:
        price_index = dict()

        for k, (f, weight) in units.items():
            price = get_price(f)
            if not price:
               continue

            taxed_price = (price * TAX_RATE) + price
            price_index[k] = (taxed_price, round(taxed_price * weight, 2))

        if any(price_index.values()):
            items.append((price_index, x))

# items.append( ({'3.5g': (28.6, 8.17) }, {'name': 'CUSTOMSALE'}) )

def sort_ppu(x):
    x = list(x[0].values())
    x.sort(key=lambda y: y[1])
    return x[0][-1]

items.sort(key=sort_ppu)
items.reverse()

for (idx, x) in items:
    print(x['name'], idx)
