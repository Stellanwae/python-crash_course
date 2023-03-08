'''take user input for a number'''
number = input('Enter a number, and i\'ll tell you if it\'s even or odd: ')
number = int(number)

if number % 2 == 0:
    print('The number {} is even'.format(number))
else:
    print('The number {} is odd.'.format(number))