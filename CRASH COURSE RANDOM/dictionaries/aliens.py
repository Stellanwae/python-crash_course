'''A list of dictionaries'''
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

'''the list of dictionaries'''
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

'''empty list for storing aliens'''
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

'''the first five aliens'''
for alien in aliens[:5]:
    print(alien)

'''Show how many aliens have been appended'''
print('The total number of aliens: {}'.format(len(aliens)))

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
for alien in aliens[:5]:
    print(alien)
    