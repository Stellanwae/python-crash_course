def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

'''making an argument optional'''
def get_formatted_name(first_name, middle_name, last_name):
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

names = get_formatted_name('stella', 'nics', 'noms')
print(names)

'''making an argument optional here'''
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name= f"{first_name} {last_name}"

    return full_name.title()
les_noms = get_formatted_name(first_name='stella', last_name='noms')
print(les_noms)

les_noms = get_formatted_name(first_name='stella', middle_name='nics', last_name='noms')
print(les_noms)