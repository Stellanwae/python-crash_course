'''positional arguments'''
def describe_pet(animal_type, pet_name):
    '''display info about the pet'''
    print('I have a {}'.format(animal_type))
    print("My {}'s name is {}".format(animal_type, pet_name.title()))

describe_pet('hamster', 'harry')
'''multiple function calls'''
describe_pet('cat', 'ROCKY')

'''order matters in positional arguments
if you mix up the order, you can get some confusions'''

'''using key words
with key words, the order is not an issue'''
describe_pet(pet_name='rocky', animal_type='dog')

'''default values
the default value comes at the right side'''
def describe_pet(pet_name, animal_type='dog'):
    print("My {}'s name is {}".format(animal_type, pet_name.title()))

describe_pet('william')

'''if the animal type i have is not a dog
must include the parameter in the function'''
describe_pet(pet_name='Rocky', animal_type='hamster')


