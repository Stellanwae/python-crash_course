class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("This is {} {}".format(self.first_name, self.last_name))
    
    def greet_user(self):
        full_name = self.first_name + " " + self.last_name
        print('Hello {}'.format(full_name))

'''different instances'''
person1 = User("John", "Smith")
person2 = User("John", "Doe")
person3 = User("Mark", "Levi")

person1.greet_user()
person1.describe_user()

print("It's been long since I saw {} {}".format(person2.first_name, person2.last_name))
person3.describe_user()
person3.greet_user()