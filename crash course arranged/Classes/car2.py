'''setting a default value for an attribute'''
class Car:
    def __init__(self, make, model, year):
        '''initialise the attributes'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        description = f"{self.make} {self.model} {self.year}"
        print(description)
    def read_odometer(self):
        print("This car has {} miles on it".format(self.odometer_reading))
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll over the odometer")
    
    '''incrementing an attributes value'''
    def increment_odometer(self, miles):
        self.odometer_reading =+ miles

'''calling a class
'''
my_car = Car("sweet", "toyota", 2020)

my_car.read_odometer()

'''modifying attribute values'''
#my_car.odometer_reading = 23
my_car.read_odometer()
my_car.update_odometer(23)
my_car.read_odometer()

my_car.update_odometer(200)
my_car.increment_odometer(100)
my_car.read_odometer()



