class Restuarant:
    '''Creating the class restuarant'''
    def __init__(self, restuarant_name, cuisine_type):
        self.restuarant_name = restuarant_name
        self.cuisine_type = cuisine_type
    
    def describe_restuarant(self):
        '''describing the restuarant'''
        print("Welcome to {}, here we have {}".format(self.restuarant_name, self.cuisine_type))
    
    def open_restuarant(self):
        '''open this restuarant'''
        print("{} is open".format(self.restuarant_name))
    
adventist_restuarant = Restuarant("Healthy foods", "vegan food")
print("I love going to {} where they server {}".format(adventist_restuarant.restuarant_name, adventist_restuarant.cuisine_type))
adventist_restuarant.describe_restuarant()
adventist_restuarant.open_restuarant()