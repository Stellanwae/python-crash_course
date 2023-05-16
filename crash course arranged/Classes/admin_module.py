from module_user_class import User
class Admin(User):
    def __init__(self, first_name, last_name, privileges=[]):
        super().__init__(first_name, last_name)
        self.privileges = privileges
    def show_priveleges(self):
        self.show_priveleges = ["can add post", "can delete post", "can ban user"]
        for i in self.show_priveleges:
            print("{}".format(i))

user1 = Admin("Some", "One")
user1.show_priveleges()