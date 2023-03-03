'''cars'''
cars = ["audi", "bmw", "subaru", "toyota"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car)
if car == "bmw":
    print("True")
else:
    print("False")

#ignoring case
cow_type = "fresian"
if cow_type.title() == "Fresian":
    print("True")
else:
    print("False")
'''using and to check multiple conditions'''
'''using or to check multiple conditions
an 'or' condition only passes when both conditions fail'''
#checking whether a value is in a list
requested_toppings = ["mushrooms", 'onions', 'pineappe']
if "mushrooms" in requested_toppings:
    print("Trueeee")
else:
    print("Falseee")
'''checking whether item is not in a list'''
banned_users = ['Andrew', 'Carolina', 'David']
user = 'Marie'
if user not in banned_users:
    print("{}, you can post a response if you wish".format(user))

'''Boolean Expressions'''
#is a conditional statement
'''Conditional Tests
Write a series of conditional tests. 
print a statement describing each test and 
your prediction of each test'''

laptop = "hp envy"
if laptop.upper() == "HP ENVY":
    print("True, it is HP ENVY")
else:
    print("False, it is not HP ENVY")

person = "STELLA"
if person.lower() == "stella":
    print("True, person is Stella")
else:
    print("this is not stella")
'''More conditional tests'''
'''age = int(input("Kindly enter your age: "))
if age > 18:
    price = 500
elif age == 18:
    price = 300
else:
    price = 150
print("This is the cost of admission {}".format(price))'''
print(requested_toppings)
requested_toppings[2] = "pineapple" 
print(requested_toppings)
alien_colour = "red"
if alien_colour == "green":
    print("{} is the colour of the alien".format(alien_colour))
elif alien_colour == "red":
    print("{} is the colour of the alien".format(alien_colour.title()))
else:
    print("False alien colour")
'''Alien colour 2'''
'''player = "green"
if player == "red":
    print("You have just earned 5 points!")
elif player is not "green":
    print("You just earned 10 points!")
alien_colour = input("please write the alien colour: ")
if alien_colour == "green":
    print("You just earned 5 points!")
elif alien_colour == "yellow":
    print("You just earned 10 points")
elif alien_colour == 'red':
    print('You just earned 15 points')'''

'''stages in life'''
'''person = int(input("Write the age of the person: "))
if person < 2:
    print("Person is a baby")
elif person >= 2 and person < 4:
    print("Person is a toddler")
elif person >= 4 and person < 13:
    print("Person is a kid")
elif person >= 13 and person < 20:
    print("Person is a teenager")
elif person >= 20 and person < 65:
    print("Person is an adult")
else:
    print('Person in an elder')'''
'''Favorite fruit'''
favourite_fruits = ['apple', 'pinepple', 'bananas']
if 'apple' in favourite_fruits:
    print('Apple is there')
if 'pineapple' is not favourite_fruits:
    print('pineapple is there')
if 'bananas' in favourite_fruits:
    print('bananas is there')
for fruit in favourite_fruits:
    if fruit == 'bananas':
        print('you really like bananas')
    else:
        print(fruit)
print(favourite_fruits)
'''using if statements with lists'''
print(requested_toppings)
for toppings in requested_toppings:
    if toppings == "onions":
        print('Sorry, we have run out of onions')
    else:
        print("{} is being added to your pizaa".format(toppings))
'''checking that a list is not empty'''

users = ['admin', 'Ashley', 'John', 'Alley', 'Nielly']
for user in users:
    if user == 'admin':
        print('Hello {}, would you like to see your report?'.format(user.title()))
    else:
        print('Welcome back {}!'.format(user.title()))
'''to make sure the list is not empty'''
if users:
    print("True")
else:
    print('we need to find some users!')
'''remove all the users'''
use = users[:]
print(use)
use = []
print(use)
if use:
    print("True")
else:
    print('we need to find some users!')
'''Checking user name'''
current_users = ['mark', 'Luke', 'John', 'Paul', 'Ruth', 'Esther']
new_users = ['Luke', 'Orphah', 'Naomi', 'Paul', 'Esther']
for user in new_users:
    if user  in current_users:
        print('We will need another user name')
    else:
        print('Welcome back {}!'.format(user))
'''ordinal numbers'''
#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in range(1, 10):
    if number == 1:
        print(f'{number}st')
    elif number == 2:
        print(f'{number}nd')
    elif number == 3:
        print(f'{number}rd')
    else:
        print(f'{number}th')

