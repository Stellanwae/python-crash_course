class Users:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    def describe_user(self):
        full_name = self.first_name + " " + self.last_name
        print(full_name)
    
    def greet_user(self):
        print(f"Hello {self.first_name}")
    
    def increment_login_attempts(self):
        self.login_attempts =+ 1
        print(self.login_attempts)
    
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(self.login_attempts)
me = Users("stella", "nicole")

me.increment_login_attempts()
me.increment_login_attempts()
me.reset_login_attempts()