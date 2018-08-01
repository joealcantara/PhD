class User():
    """ First attempt at describing a user """
    
    def __init__(self, fname, lname):
        """ Initialise attributes """
        self.fname = fname
        self.lname = lname
        self.login_att = 0

    def describe_user(self):
        print("First Name : " + self.fname)
        print("Last Name : " + self.lname)

    def greet_user(self):
        print("Hello, " + self.fname.title() + " " + self.lname.title() + ".")
    
    def increment_login_attempts(self):
        self.login_att += 1
    
    def reset_login_attempts(self):
        self.login_att = 0

user1 = User("Joe", "Alcantara")
user2 = User("Lexi", "Belle")
user3 = User("Hailey", "Little")

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()

user3.increment_login_attempts()
print(user3.login_att)
user3.increment_login_attempts()
print(user3.login_att)
user3.increment_login_attempts()
print(user3.login_att)
user3.increment_login_attempts()
print(user3.login_att)
user3.reset_login_attempts()
print(user3.login_att)