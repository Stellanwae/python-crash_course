class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_description = f"{self.make} {self.model} {self.year}"
        print(long_description.title())

my_first_car = Car("range rover", "Mercedes Benz", 2023)
my_first_car.get_descriptive_name()

'''Setting a default value for an attribute'''
