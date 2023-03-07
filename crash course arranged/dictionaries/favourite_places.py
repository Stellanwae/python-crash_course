favourite_places = {
    'luke': ['panama', 'hawaii', 'zanzibar'],
    'mark': ['egypt', 'israel', 'pemba'],
    'tabitha': ['morocco', 'australia', 'paris'],
}

for k, v in favourite_places.items():
    print('{} loves the following places:'.format(k.title()))
    for val in v:
        print('\t{}'.format(val.title()))