favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
friends = ['jen', 'sarah', 'edward', 'phil', 'james', 'jane', 'jonah']
for name in friends:
    if name not in favourite_languages.keys():
        print('{}, you should take the poll please'.format(name.title()))
    else:
        print('Thank you for taking the poll')
