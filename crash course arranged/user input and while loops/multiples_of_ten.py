'''ask for a number'''
number = int(input('Write a number, and we\'ll tell you if it\'s a multiple of ten or not. '))

if number % 10 == 0:
    print('It\'s a multiple of ten')
else:
    print("It's not a multiple of ten")
