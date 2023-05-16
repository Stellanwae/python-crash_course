class Dog:
    '''A simple attempt to model a dog'''

    def __init__(self, name, age):
        '''initialising the attributes'''
        self.name = name
        self.age = age

    def sit(self):
        '''Making a dog sit'''
        print('Now {} is sitting'.format(self.name))
    
    def rollover(self):
        '''Make the dog roll over'''
        print('{} is rolling over'.format(self.name))

'''using the class'''
my_dog = Dog('Spike', 3)

print("My dog's name is {} and he is {} years old".format(my_dog.name, my_dog.age))

'''calling the methods'''
my_dog.sit()
my_dog.rollover()