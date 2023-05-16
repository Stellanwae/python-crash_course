'''Using Python standard library'''

from random import randint

number = randint(1,6)
print(number)

from random import choice
players = ["charles", "martina", "michael", "florence", "eli"]
first_up = choice(players)
print(first_up)

