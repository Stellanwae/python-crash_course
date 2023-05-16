class Restuarant:
    def __init__(self, restuarant_name, cuisine_type):
        self.restuarant_name = restuarant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restuarant(self):
        '''describing my restuarant'''
        print(f"This is {self.restuarant_name}, it serves {self.cuisine_type}")
    
    def open_restuarant(self):
        '''that print the restuarant is open'''
        print(f"{self.restuarant_name} is open")
    
    def set_number_served(self, number):
        '''number the restuarant served'''
        self.number_served = number
    def print_number_served(self):
        print(f'{self.number_served} is the number served')
    
    def increment_number_served(self, number1):
        self.number_served =+ number1

my_restuarant = Restuarant("Bellah Bakes", "african vegan dishes")

my_restuarant.describe_restuarant()
my_restuarant.open_restuarant()
my_restuarant.number_served = 46
print(f"This is the number served = {my_restuarant.number_served}")

my_restuarant.set_number_served(290)
my_restuarant.increment_number_served(45)
my_restuarant.print_number_served()
#my_restuarant.increment_number_served(45)
my_restuarant.print_number_served()
'''This one not incrementing'''
