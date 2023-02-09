person = {'fname':'Stella', 'lname': 'Nwae', 'weight': 48}
for key in person.keys():
    print(key)
print('\n')
for value in person.values():
    print(value)
print('\n')
for k, v in person.items():
    print(k, v)

dictionary = {'well': 'Jacob\'s', 'height': 56}
dictionary1 = {'well': 'econt', 'height': 45}
dictionary2 = {'well': 'jabalic', 'height': 56}
dict_list = [dictionary, dictionary1, dictionary2]
print(dict_list)
for list in dict_list:
    print(list)

for list in dict_list:
    if list['well'] == 'econt':
        list['well'] = 'yales'
    if list['height'] == 56:
        list['height'] = 50
    print('this is a list: {}'.format(list))
print(dict_list)
