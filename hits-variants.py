#!/usr/bin/env python3
#####
# finds the top level variants of items
# inside of algoliasearch response field in
# 'hits'
###
import json

with open('response.json') as fd:
    results = json.loads(fd.read())

variants = set()
for x in results['hits']:
    variants.add(tuple(x.keys()))

print(f"result['hits'] variants: {len(variants)}")

# largest item must be at the beginning (for set.difference)
tup = list(variants)
tup.sort(reverse=True, key=lambda x: len(x))

r = set.difference(*(set(x) for x in tup))
print(f'unique fields: {r}')
