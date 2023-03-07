players = ['charles', 'martina', 'michael', 'florence', 'eli']

'''the first three'''
print('The first three items in the list are:')
for player in players[:3]:
    print(player)

print('The three items in the middle of the list are:')
print(players[1:-1])

'''the last three'''
print('The last three items in the list are:')
print(players[2:])