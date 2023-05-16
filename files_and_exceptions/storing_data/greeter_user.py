import json

filename = 'name.json'
with open(filename) as f:
    name = json.load(filename)

print(f'Welcome back {name}')