'''while loop
counting 1 to 5 using while loop'''
'''current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1'''
prompt = '\nTell me something, and I will repeat it back to you'
prompt += '\nEnter \'quit\' to end the program '
'''message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)'''


'''
active = True
while active:
    message = input('Tell me something, and I will repeat it back to you ')

    if message == 'quit':
        active = False
    else:
        print(message)
'''


'''Using break to exit a loop'''

'''while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print('I\'d love to go to {}'.format(city.title()))'''

'''Using continue in a loop'''
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

'''Avoiding infinite loops'''
x = 1
while x <= 5:
    print(x)
    x += 1


'''Try it yourself'''
'''Pizza toppings
write a loop that promts the user to enter a series of 
pizza toppings until they enter a 'quit' value.
as they enter each topping, print a message saying 
you'll add that topping to their pizza'''

'''active = True
while active:
    message = input('Which topping would you like?')
    if message == 'quit':
        active = False
    else:
        print('Adding {} topping to your pizza'.format(message))'''

'''Movie tickets'''
'''input to ask the age of a person'''
'''age = int(input('What is your age? '))
if age > 0 and age < 3:
    print('The ticket is free')
elif age >= 3 and age <= 12:
    print('Ticket is $10')
else:
    print('Ticket is $15')'''


'''Using a while loop with lists and dictionaries'''
'''moving items from one list to another'''
unconfirmed_users = ['Walter', 'Wekesa', 'Bravin']
confirmed_users =[]
while unconfirmed_users:
    current_users = unconfirmed_users.pop()
    print('Current user: {}'.format(current_users))
    confirmed_users.append(current_users)
    print('{}'.format(confirmed_users))
'''removing all instances of specific values from a list'''
pets = ['dog', 'cat', 'goldfish', 'rabbit', 'cat']
print('These are the pets we have:')
for pet in pets:
    print('\t\t\t{}'.format(pet))
while 'cat' in pets:
    pets.remove('cat')
print(pets)
'''Filing a dictionary with user input'''
'''name = input('What is your name? ')
favourite_mountain = input('Which mountain would you like to climb? ')
response = {}
response[name] = favourite_mountain

for nam, resp in response.items():
    print('{}\'s favourite mountain is {}'.format(nam, resp))'''


'''Try it yourself'''
'''A list called sandwich_orders'''
sandwich_orders = ['peanut butter', 'blueband', 'avocado', 'chocolate', 'desicated coconut']
finished_sandwiches = []
for sandwich in sandwich_orders:
    print('I made your {} sandwich'.format(sandwich))
    finished_sandwiches.append(sandwich)
print(finished_sandwiches)
print('The following sandwiches have been made: ')
for sandwich in finished_sandwiches:
    print('\t\t\t{}'.format(sandwich))

'''No pastrami'''
'''Ensure pastrami appears at least three times in your list'''
sandwich_orders.append('pastrami')
sandwich_orders.append('pastrami')
sandwich_orders.append('pastrami')
sandwich_orders.append('pastrami')
print(sandwich_orders)
print('We have run out of pastrami')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    for sandwich in sandwich_orders:
        print('{}'.format(sandwich))
print('\n')


'''Dream vacation'''
active_poll = True
user_poll = {}
while active_poll:
    poll_agreement = input('Would you like to take this poll?(yes or no) ')
    if poll_agreement == 'no':
        active_poll = False
        break
    name = input('What is your name? ')
    place = input('Where would you go? ')

    user_poll[name] = place
    for nam, plc in user_poll.items():
        print('{}\'s favourite vacation place is {}'.format(nam, plc))


