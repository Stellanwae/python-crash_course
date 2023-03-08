'''returning a dictionary'''
def build_person(first_name, last_name):
    person = {}
    person['first'] = first_name
    person['last'] = last_name

    return person
personne = build_person('James', 'Allen')
print(personne)

'''puting more meaningful data'''
def build_person(first_name, last_name, age=None):
    person = {}
    person['first'] = first_name
    person['last'] = last_name
    if age:
        person['age'] = age
    return person
les_noms = build_person(first_name='stella', last_name='noms', age=25)
print(les_noms)