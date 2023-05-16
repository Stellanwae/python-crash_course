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
    
class IceCreamStand(Restuarant):
    def __init__(self, restuarant_name, cuisine_type, flavour):
        super().__init__(restuarant_name, cuisine_type)
        self.flavour = flavour
    
    def list_flavour(self):
        for i in self.flavour:
            print("{}".format(i))
    
'''calling list_flavour method'''
flavours = ["vanilla", "strawberry", "chocolate"]
ice_cream = IceCreamStand("Churchill", "ice cream", flavours)

ice_cream.list_flavour()
