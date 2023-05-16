import json

filename = 'numbers.json'
with open(filename) as f:
    readit = json.load(f)

print(readit)