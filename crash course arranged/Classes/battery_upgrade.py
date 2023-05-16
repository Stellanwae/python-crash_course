class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def get_descriptive_name(self):
        print(f"{self.make} {self.model} {self.year}")

class Battery:
    def __init__(self, battery_size = 75):
        '''the 75 is a default value'''
        self.battery_size = battery_size
    def upgrade_battery(self):
        #if self.battery_size != 100:
        self.battery_size = 100
            #print(self.battery_size)
  
    def describe_battery(self):
        print(f"This car has {self.battery_size}-kwh battery")

   

    def get_range(self):
        '''A statement about the range this car provides'''
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315


'''Inheritance'''
class ElectricCar(Car):
    def __init__(self, model, make, year):
        super().__init__(make, model, year)
        self.battery_size = 75
        self.battery = Battery()

car = ElectricCar("tesla", "s3", 2023)
car.battery.describe_battery()
car.battery.upgrade_battery()
car.battery.get_range()
