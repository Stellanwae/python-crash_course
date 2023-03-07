alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

'''working with dictionaries'''
alien_0 = {'color': 'green', 'points': 5}

'''accessing values in a dictionary'''
new_points = alien_0['color']
print('You just earned new points'.format(new_points))

'''adding new key and value pairs'''
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

'''starting with an empty dictionary'''
alien_0 = {}

'''adding values to the empty list'''
alien_0['color'] = 'green'

print(alien_0)

'''Modifying the color in a dictionary'''
alien_0['color'] = 'yellow'
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['speed'] = 'medium'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #This must be a fast alien
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print('New position: {}'.format(alien_0['x_position']))


'''Removing key value pairs
using the del function'''
print(alien_0)
del alien_0['color']
print(alien_0)



