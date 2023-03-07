'''looping using the glossary exercise'''
glossary = {
    'del': 'to delete values in list and dictionaries',
    'remove': 'another way to delete',
    'list comprehensions': 'how to write short codes',
    'get()': 'To check if there\'s something in a list',
    'list()': 'To make a list'
}

for key, value in glossary.items():
    print('{}: {}'.format(key, value))
