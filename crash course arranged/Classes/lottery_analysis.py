from random import choice
my_ticket = [38, 78, 65, 52, 17, 87]
j = 0
winning_numbers = [52, 17, 87]
for i in range(len(my_ticket)):
    if my_ticket[i] == choice(my_ticket):
        print(i)