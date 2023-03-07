favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for name, language in favourite_languages.items():
    print('{}\'s favourite language is {}'.format(name.title(), language.title()))

'''Looping through all the keys
making a list in the process'''
friends = []
for name in favourite_languages.keys():
    friends.append(name)
    print(name.title())
    if name in friends:
        language = favourite_languages[name].title()
        print('{}, I see you love {}'.format(name.title(), language))
print(friends)

friends = ['jen', 'sarah', 'edward', 'phil']

if 'erin' not in favourite_languages.keys():
    print('Erin, please take your poll')


'''Looping with a certain order'''
for name in sorted(favourite_languages.keys()):
    print(f'{name.title()}, thank you for taking the poll')

'''Looping through all the values in a dictionary'''
print('The following languages are mentioned:')
for lang in favourite_languages.values():
    print(lang.title())


'''making a set'''
for lang in set(favourite_languages.values()):
    print(lang)

lang = set(favourite_languages.values())
print(lang)
