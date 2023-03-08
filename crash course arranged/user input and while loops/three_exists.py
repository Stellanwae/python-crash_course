age = int(input('give your age '))
while age < 3:
    print('ticket is free')
    break
while age >= 3 and age < 12:
    print('price is 10 dollars')
    break
while age >= 12:
    print('Price is 15 dollars')
    break

active = True
while active:
    age = int(input('what\'s your age? '))
    if age < 3:
        print('Free!')
        break
    elif age >= 3 and age < 12:
        print('Pay 10 dollars')
        break
    else:
        print('Pay 15 dollars')
        break