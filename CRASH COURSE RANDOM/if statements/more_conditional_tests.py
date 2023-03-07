'''test for equality with strings'''
my_name = 'acapella'
if my_name == 'acapella':
    print('True')
else:
    print('False')

'''Test using the lower method'''
friend = 'Holmes'
if friend.lower() == 'holmes':
    print('True')
else:
    print('False')

'''numerical tests involving equality'''
age = 18
if age > 22:
    print('True')
else:
    print('False')

'''using the 'and' key word'''
if age < 21 and age > 15:
    print('This is true')

'''or keyword
'''
if age < 21 or age > 54:
    print('Is a true statement')

'''test whether item is in a list'''
new_list = ['one', 'two', 'three', 'four']
num = 'six'
if num in new_list:
    print('One is here')
'''when item is not in list'''
if num not in new_list:
    print('it\'s not here')