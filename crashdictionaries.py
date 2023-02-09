'''simple dictionary'''
alien_0 = {'colour': 'green', 'points': 5}
print(alien_0['colour'])
print(alien_0['points'])
'''working with dictionaries
composed of key value pairs
use a key to access the value associated
key is on the left side of the colon
dictionary is wrapped in curly braces
the simplest dictionary contains only one key value pair'''
'''simple dictionary 1'''
alien = {'colour':'blue', 'points': 10}
print(alien)
print(alien['colour'])

new_points = alien['points']
print('You just earned {} points!'.format(new_points))
new_list = [10, 23, 34]
part = new_list[1]
print('Here\'s what you just earned: \n{} points'.format(part))
'''Adding new key-value pairs'''
alien['height'] = 163
alien['weight'] = 50
print(alien)
'''Starting with an empty dictionary'''
empty_dictionary = {}
empty_dictionary['blue'] = 'the colour of the sky'
empty_dictionary['oxford'] = 'new dictionary edition'
print(empty_dictionary)
'''Modifying the values in a dictionary'''
dict = {}
dict['colour'] = 'blue'
dict['pages'] = 1234
print('The dictionary has the colour {}'.format(dict['colour']))
dict['colour'] = 'yellow'
print('The dictionary has the colour {}'.format(dict['colour']))
'''tracking the position of an alien'''
alieno = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print('Original position: {}'.format(alieno['x_position']))
if alieno['speed'] == 'slow':
    x_increment = 1
elif alieno['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
#the new postion
alieno['x_position'] = alieno['x_position'] + x_increment
print('New position: {}'.format(alieno['x_position']))
print(alieno)
'''A dictionary of similar objects'''
favourite_languages = {
    'jen': 'Python',
    'Sarah': 'C',
    'Edward': 'Ruby',
    'Phil': 'Python'
}
print(favourite_languages)
print('Phil\'s favourite language is {}'.format(favourite_languages['Phil']))
'''using get() to access values'''
print(alieno)
print(alieno.get('points', 'No point value assigned'))
print(alieno.get('points'))
'''try it yourself: person'''
person = {'fname': 'Lebanon', 'lname': 'Hill', 'age': 45, 'city': 'Houston'}
print(person)
print(person['fname'])
print(person['lname'])
print(person['age'])
print(person['city'])
print(person.get('height', 'Not found in dictionary'))
'''Favourite numbers'''
favourite_numbers = {'Stella': 8, 'Mary': 7, 'Jayden': 2, 'Baron': 1} 
print('Stella\'s favourite number is {}'.format(favourite_numbers['Stella']))
print('Mary\'s favourite number is {}'.format(favourite_numbers['Jayden']))
print('Jayden\'s favourite number is {}'.format(favourite_numbers['Mary']))
print('Baron\'s favourite number is {}'.format(favourite_numbers['Baron']))
'''Glossary'''
glossary = {'print':'Function that prints output', 'constant': 'a number that remains unchanged in a list',
'looping': 'passing a value a number of times'}
'''Looping through a dictionary'''

'''Looping through all key-value pairs'''
user = {
    'username': 'Ifeoma',
    'userage': 34,
    'userheight': 167
}
for key, value in user.items():
    print(key, ":", value)
for key, value in glossary.items():
    print(key, ":", value)
for name, language in favourite_languages.items():
    print(name, ":", language)
    print('{}\'s favourite language is {}'.format(name, language))
'''Looping through keys in a dictionary'''
for key in favourite_languages.keys():
    print(key)
'''or you can do it without the keys() function
Becausee the keys is the default behaviour when looping through a dictionary'''
for name in favourite_languages:
    print(name)
print('This is the favourite languages keys')
print('right here')
friends = ['Phil', 'Sarah']
for name in favourite_languages.keys():
    print(name.title())
    if name in friends:
        language = favourite_languages[name].title()
        print('{}, I see you love {}'.format(name.title(), language))

favourite_numbers = {'Stella': 8, 'Mary': 7, 'Jayden': 2, 'Baron': 1}
names = ['Stella', 'Jayden']
for name in favourite_numbers.keys():
    print(name.title())
    if name in names:
        number = favourite_numbers[name]
        print('{}\'s favourite number is {}'.format(name, number))
print(favourite_languages.get('Phil'))
for key, value in favourite_numbers.items():
    print("this is the key: {}\nThis is the value: {}".format(key, value))
'''Looping through all values in a Dictionary'''
'''To print the values of keys in a dictionary
without the keys, we use the values() method 
to return the key'''
print('These are the favourite language polls:')
for value in favourite_languages.values():
    print(value)
'''when working with values, some can be repeated
This is easy to sort when working with a small dictionary
But, when it involves millions, a set() method will do the trick'''
double_values = {'vaen': 'python', 'ursla': 'python', 'janet': 'ruby', 'yolanda': 'ruby'}
for value in set(double_values.values()):
    print(value.upper())
'''i'm not sure i set() method also works with the key() method'''
'''i think it does
'when you wrap a set() around a list that contains duplicate
items, Python identifies the unique items in the list and builds a set from 
those items '''
'''set
You can build a set directly by separating elements with commas'''
languages = {'python', 'ruby', 'python', 'c'}
print(languages)#it won't repeat python/ duplicate python is automatically removeed


'''Try it yourself'''
glossary2 = {'presumptions': 'preconceived notions', 'detective': 'someone investigating something'}
for k, v in glossary2.items():
    print(k, v)
glossary2['open mind'] = 'no presumptions'
glossary2['evidence'] = 'like to call it faith'
for k, v in glossary2.items():
    print('{}: {}'.format(k.title(), v))


'''Rivers'''
rivers = {'Nile': 'Egypt', 'Tana': 'Kenya', 'Amazon': 'America'}
for k, v in rivers.items():
    print('The {} runs through {}'.format(k, v))


'''To include the name of each river in the dictionary'''
for river in rivers:
    print('{} is a river'.format(river))


'''Include the name of each country'''
for country in rivers.values():
    print('{} has a river'.format(country))


'''Polling'''
print(languages)
print(favourite_languages)
favourite_languages['Jack'] = 'c++'
favourite_languages['Sarah'] = 'js'
people = ['Sarah', 'Edward']
for name in favourite_languages:
    if name in people:
        print('Thanks {} for taking the poll'.format(name))
    else:
        print('{}, please take the poll'.format(name))


'''Nesting'''
'''A list of dictionaries'''
'''when you want to store dictionaries in a list'''
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)


'''when you want to append a list of thirty more aliens to the existing alien list'''
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)


for alien in aliens[:5]:
    print(alien)


'''the total number of aliens on the list'''
print(len(aliens))


'''To modify the aliens in the list'''
'''The list of dictionaries
since the dictionaries have the same keys all through
you can use for loop and if statements to change the values '''
for alien in aliens:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10


'''A list in a dictionary'''
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}
print(pizza)
for key, value in pizza.items():
    print(key)
    for val in value:
        print(val)
print('These are the pizza topping: ')
for piz in pizza['toppings']:
    print('\t' + piz)


favourite_languages = {
    'jen': ['python', 'ruby'],
 'sarah': ['c'],
 'edward': ['ruby', 'go'],
 'phil': ['python', 'haskell'],
}
for name, languages in favourite_languages.items():
    print('{}\'s favourite languages are:'.format(name.title()))
    for lan in languages:
        print('\t' + lan)


'''A dictionary in a dictionary'''
users = {
    'alien': {
    'first': 'Bowman', 
    'last': 'capsule',
    'location': 'Princeton'
    },
    'mcurie':{
        'first': 'marie',
        'last': 'curie', 
        'location': 'paris'
    } 
    }
for username, userinfo in users.items():
    print('Username: {}'.format(username.title()))
    full_name = '{} {}'.format(userinfo['first'], userinfo['last'])
    location = userinfo['location']

    print('\tFull name: {}'.format(full_name.title()))
    print('\tLocation: {}'.format(location))


'''Try it yourself'''
'''People'''

'''make two dictionaries'''
jayden = {'fname': 'Jayden', 'lname': 'Adrian', 'gender': 'male'}
ronald = {'fname': 'Ronald', 'lname': 'Vance', 'gender': 'male'}
'''make a list of the two dictionaries'''
people = [jayden, ronald]
'''Looping through the list of people'''
for pep in people:
    full_name = '{} {}'.format(pep['fname'], pep['lname'])
    gender = '{}'.format(pep['gender'])
    print('\nFull name: {}'.format(full_name))
    print('Gender: {}'.format(gender))


'''pets'''

'''making dictionaries containing pets'''
pet_1 = {'Kind': 'Dog', 'Owner': 'Cowell'}
pet_2 = {'Kind': 'Rabbit', 'Owner': 'Praise'}
pet_3 = {'Kind': 'Squirrel', 'Owner': 'Sophy'}
pet_4 = {'Kind': 'Cat', 'Owner': 'Jayden'}
pet_5 = {'Kind': 'Chihuahua', 'Owner': 'Smith'}

'''Storing dictionaries into list'''
pets = [pet_1, pet_2, pet_3, pet_4, pet_5]

'''printing everything about the pet using a loop'''
for pet in pets:
    kind = pet['Kind']
    owner = pet['Owner']
    print('{} owns a {}'.format(owner, kind))


'''Favourite places'''


favourite_places = {'James': ['Paris', 'Hawaai'], 'John': ['Princeton', 'Johanessburg'], 'Peter': ['Corinth', 'Belmont', 'London']}
'''looping through everything in a loop'''

for person, favplace in favourite_places.items():
   print('{}\'s favourite places are: '.format(person)) 
   for place in favplace:
    print('\t{}'.format(place))


'''Favourite numbers'''
print(favourite_numbers)
favourite_numbers = {'Stella': [8, 9, 2], 'Mary': [7, 14, 21], 'Jayden': [2, 4, 6], 'Baron': [1, 2, 3, 4]} 
for person, favnom in favourite_numbers.items():
    print('{}\'s favourite numbers are: '.format(person), end='')
    for fav in range(len(favnom)):
        if fav < (len(favnom)-1):
            print('{}, '.format(favnom[fav]), end='')
        else:
            print('{}'.format(favnom[fav]))


'''cities'''

'''dictionary called cities'''
cities = {
    'Nairobi': {
        'country': 'kenya', 
        'population': 3000000, 
        'fact': 'rowdy'
        }, 
        'Johanessburg': {
            'country': 'south africa',
            'population': 4000000,
            'fact': 'mixed races'
        }, 
        'Paris':
        {
            'country': 'france',
            'population': 2000000,
            'fact': 'tour eiffel'
        }}

'''printing name of each '''
for city, info in cities.items():
    print('{} is a city'.format(city), end='')
    country = info['country'].title()
    population = info['population']
    fact = info['fact'].title()
    print(' in {} and has the population of {}.\nIt is known for {}'.format(country, population, fact))
print(cities)
cities['Kisumu'] = {'country': 'kenya', 'population': 2000000, 'fact':'fish and omena'}
print(cities)
for city, info in cities.items():
    print('{} is a city'.format(city), end='')
    country = info['country'].title()
    population = info['population']
    fact = info['fact'].title()
    print(' in {} and has the population of {}.\nIt is known for {}'.format(country, population, fact))
    