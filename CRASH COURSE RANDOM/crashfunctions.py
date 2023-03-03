list = [45, [23]]
print(list)
#print as a matrix
def matrixo(matrix = [[]]):
    for mat in matrix:
        print(mat)
my_matrix = [[1, 2, 3, 4], [2, 4, 5], [3, 4, 7]]
matrixo(my_matrix)

#passing information to a function
def greet_user(username):
    print('Hello {}'.format(username.title()))

greet_user('stella')

import this
'''Message'''
def display_message():
    print('Hey there! I am learning about functions in this chapter')
display_message()

'''Favourite book'''
def favourite_book(title):
    print('{}'.format(title.title()))

book = 'Back to Eden'
favourite_book(book)
#positional arguments
def describe_pet(animal_type, pet_name):
    print('I have a {}'.format(animal_type))
    print('My {}\'s name is {}'.format(animal_type, pet_name.title()))
describe_pet('squirrel', 'squeaky')

'''Order matters in positional arguments'''
'''default name'''
def describe_pet(pet_name, animal_type = 'dog'):
    print('I have a {}'.format(animal_type))
    print('My {}\'s name is {}'.format(animal_type, pet_name))
describe_pet('Willie')
'''The non-default value comes first then the default value follows'''
describe_pet('Spike', 'Cat')

'''Try it yourself'''
# def make t-shirt
#accepts an int size
# and text of a message to be printed out
#print out the sentence summarizing the size of the shirt
# and the message printed on it
def make_shirt(size, message):
    print('The size of your shirt is {} and \'{}\' is printed on it'.format(size, message))

file = 'Accepted in the beloved'
sz = 'small'
make_shirt(sz, file)
make_shirt(message= 'Black lives matter', size='extra large')

'''Large shirts'''
# uses the same make_shirt function
# default message is "i love python"
# large and medium shirts share the default message

def make_shirt(message = 'I love python', size = 'large'):    
    print('The size of the shirt is {} and the message is \'{}\'.'.format(size, message) )

#defaults in action

make_shirt()

#a shirt of any size and a different message

make_shirt(size ='small', message='atomic habits')

#cities
'''the function describe_city()'''
#should take city and country
#print message {city} is in {country}
#parameter for country should have a default value

def describe_city(city, country='Iceland'):

    print('{} is in {}'.format(city, country))

#1st city
describe_city('Nairobi', 'Kenya')

#2nd city
describe_city('Kigali', 'Rwanda')

#3rd city
describe_city('ice city')
'''The value that a function returns is called a return value'''

#Returning a simple value

def get_formatted_name(first_name, last_name):
    full_name = '{} {}'.format(first_name, last_name)
    return full_name
name = get_formatted_name('Stella', 'Nwae')
print(name)

'''Making an argument optional'''

def make_shirt(message='', size='large'):
    if size == 'medium' or size == 'large':
        message = 'I love python'
    print('The size of your shirt is {} and it is printed {}'.format(message, size))
make_shirt(size='medium')
