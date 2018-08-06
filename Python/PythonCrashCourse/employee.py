class Employee():
    """ A simple model of an employee """
    def __init__(self, fname, lname, salary):
        self.fname = fname.title()
        self.lname = lname.title()
        self.salary = salary

    def give_raise(self, amount=5000):
        self.salary += amount
