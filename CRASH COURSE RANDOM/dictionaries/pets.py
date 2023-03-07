pet1 = {'type': 'dog', 'owner': 'mike'}
pet2 = {'type': 'cat', 'owner': 'miriam'}
pet3 = {'type': 'sheep', 'owner': 'william'}
pets = [pet1, pet2, pet3]

for pet in pets:
    for k, v in pet.items():
        type = pet['type']
        owner = pet['owner']
    print('{} has a {}'.format(owner.title(), type))