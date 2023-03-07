favorite_languages = {
 'jen': ['python', 'ruby'],
 'sarah': ['c'],
 'edward': ['ruby', 'go'],
 'phil': ['python', 'haskell'],
 }

'''
printing the key
printing the values'''

for name, value in favorite_languages.items():
        print('{}\'s favourite languages are:'.format(name))
        for val in value:
            print('\t{}'.format(val))



