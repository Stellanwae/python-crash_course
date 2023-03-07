'''A list in a dictionary'''
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print('You ordered a {} -- pizza crust with the following toppings:'.format(pizza['crust']))
for topping in pizza['toppings']:
    print(topping)
