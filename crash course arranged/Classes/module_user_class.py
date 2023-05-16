class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("This is {} {}".format(self.first_name, self.last_name))
    
    def greet_user(self):
        full_name = self.first_name + " " + self.last_name
        print('Hello {}'.format(full_name))