class User:

    def __init__(self, first_name, last_name, age, location):
        self.f_name = first_name
        self.l_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print("users name : "+ self.f_name + " " + self.l_name)
        print("users age : "+ str(self.age))
        print("users location: " +self.location)

    def greet_user(self):
        print(f"hello {self.f_name} {self.l_name} ")

    def user_location(self):
        print(f"{self.f_name} lives in {self.location}")

    def increment_login_attempts(self):
        """ increase login attempts by """
        self.login_attempts += 1

    def reset_login_attempts(self):
        """ reset the number of login attempts """
        self.login_attempts = 0    

    def login_attempt(self):
        """ print number of login attempts """
        print(f"users login tries: {self.login_attempts} ")


user1 = User('leonardo','david',19,'avadi')

user1.describe_user()
user1.greet_user()
user1.user_location()

user1.increment_login_attempts()
user1.login_attempt

user1.increment_login_attempts()
user1.login_attempt()

user1.reset_login_attempts()
user1.login_attempt()