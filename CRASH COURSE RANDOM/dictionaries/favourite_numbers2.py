favourite_numbers = {
    'goldsmith': [7, 5, 6],
    'lavenda': [8, 4, 9],
    'ida': [7, 6,3],
    'mama': [10, 2, 12],
    'southampton': [1, 3, 4],
}

for k, v in favourite_numbers.items():
    print('{}\'s favourite numbers are:'.format(k))
    for val in v:
        print('\t{}'.format(val))