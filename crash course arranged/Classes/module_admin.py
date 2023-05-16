class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("This is {} {}".format(self.first_name, self.last_name))
    
    def greet_user(self):
        full_name = self.first_name + " " + self.last_name
        print('Hello {}'.format(full_name))

class Admin(User):
    def __init__(self, first_name, last_name, privileges=[]):
        super().__init__(first_name, last_name)
        self.privileges = privileges
    def show_priveleges(self):
        self.show_priveleges = ["can add post", "can delete post", "can ban user"]
        for i in self.show_priveleges:
            print("{}".format(i))
        
