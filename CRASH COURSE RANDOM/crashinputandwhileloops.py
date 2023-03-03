'''User input and while loops'''


'''Try it yourself
'''
'''Rental car'''
'''ask user about the rental car they want'''

'''rental_car = input('What kind of rental car would you like? ')
print('Lemme see if I can find you a {}'.format(rental_car))'''

'''Restuarant seating'''

'''ask user how many people are in the dinner group'''
'''dinner_group = int(input('How many people are in the dinner group? '))
if dinner_group > 8:
    print('You\'ll have to wait for a table')
elif dinner_group > 0: 
    print('Your table is ready!')
else:
    print('Invalid number!')'''


'''Multiples of ten'''
number = int(input('Write a number: '))
if number % 10 == 0:
    print('it\'s a multiple of ten')
else:
    print('it\'s not a multiple of ten')
    