users = {
 'aeinstein': {
 'first': 'albert',
 'last': 'einstein',
 'location': 'princeton',
 },
 'mcurie': {
 'first': 'marie',
 'last': 'curie',
 'location': 'paris',
 },
 }
print(users)
'''accessing dictionary within a dictionary'''
print('This is a dictionary within a dictionary')
for name, value in users.items():
    full_name = value['first'] + ' ' + value['last']
    location = value['location']
    print('Username: {}'.format(name.title()))
    print('\tFull name: {}'.format(full_name.title() ))
    print('\tlocation: {}\n'.format(location.title()))