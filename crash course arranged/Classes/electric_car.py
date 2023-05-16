class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def get_descriptive_name(self):
        print(f"{self.make} {self.model} {self.year}")


'''Inheritance'''
class ElectricCar(Car):
    def __init__(self, model, make, year):
        super().__init__(make, model, year)
        self.battery_size = 75
    
    def describe_battery(self):
        print(f"This car has {self.battery_size}-kwh battery")


my_tesla = ElectricCar("S3", "Tesla", 2022)
my_tesla.get_descriptive_name()
my_tesla.describe_battery()


class Battery:
    def __init__(self, battery_size = 75):
        '''the 75 is a default value'''
        self.battery_size = battery_size
    
    def describe_battery(self):
        print(f"This car has {self.battery_size}-kwh battery")

    def get_range(self):
        '''A statement about the range this car provides'''
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print("This car can go about {} miles in a full charge".format(range))
my_battery = Battery(100)
my_battery.describe_battery()
my_battery.get_range()

