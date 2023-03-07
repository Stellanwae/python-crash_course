cities = {
    'nairobi': {
    'country': 'kenya',
    'population': 2000000,
    'fact': 'the capital city of kenya',
    },
    'mombasa':{
    'country': 'kenya',
    'population': 3000000,
    'fact': 'have interesting dishes',
    },
    'kisumu':{
    'country': 'kenya',
    'population': 3000000,
    'fact': 'the home of delicious fish',
    },
}

for k, v in cities.items():
    print('The are all you need to know about {}'.format(k.title()))
    for key, value in v.items():
        if value == v['country']:
            print('{}: {}'.format(key.title(), value.title()))
        else:
            print('{}: {}'.format(key.title(), value))

cities['cairo'] = {
    'country': 'egypt',
    'population': 2500000,
    'fact': 'known for sphinx',
}

print(cities)
