answer = 17

if answer != 42:
    print('that is not the correct answer. Please try again.')

'''using and to check multiple conditions'''
age_0 = 22
age_1 = 18

if age_0 > 20 and age_1 < 21:
    print('True')

'''using or'''
if age_0 > 23 or age_1 < 21:
    print('True')
else:
    print('False')

'''checking whether a value is in a list'''
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if "mushrooms" in requested_toppings:
    print('Mushrooms here, True')
