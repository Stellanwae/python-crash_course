person = {'first name': 'Randy', 'second name': 'skeete', 'age': 50, 'city': 'London'}
person1 = {'first name': 'sir', 'second name': 'tim', 'age': 60, 'city': 'Paris'}
person2 = {'first name': 'Burners', 'second name': 'Lee', 'age': 45, 'city': 'Austria'}

people = [person, person1, person2]
print(people)

for prsn in people:
    for k, v in prsn.items():
        full_name = '{} {}'.format(prsn['first name'], prsn['second name'])
        location = '{}'.format(prsn['city'])
        age = '{}'.format(prsn['age'])
    print('{} lives in {} and is {} years old'.format(full_name, location, age))

