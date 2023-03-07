'''checking for special items'''
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for topping in requested_toppings:
    print('Adding {}'.format(topping))

for topping in requested_toppings:
    if topping == 'green peppers':
        print('Sorry, we are out of green peppers right now')
    else:
        print('Adding {}'.format(topping))

requested_toppings = []
if requested_toppings:
    for topping in requested_toppings:
        print('Adding {}'.format(topping))
    print('Finished making your pizza')
else:
    print('Are you sure you want plain pizza')


'''using multiple lists'''
available_toppings = ['mushrooms', 'olives', 'green peppers',
 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for topping in requested_toppings:
    if topping in available_toppings:
        print('Adding {}'.format(topping))
    else:
        print('Sorry, we don\'t have {}'.format(topping))
    