class Car():
    """ A simple attempt to represent a car """

    def __init__ (self, make, model, year):
        """ Initialize attributes to describe a car """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name (self):
        """ Return a neatly formatted descriptive name """
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()
    def read_odometer(self):
        """ Prints a statement showing the car's current mileage """
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self, mileage):
        """ 
        This takes in a value for mileage and updates the value 
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """
        This function takes in a value and increments the odometer by the value.
        """
        self.odometer_reading += miles

my_new_car = Car('Audi', 'A6', 2016)
# my_new_car.odometer_reading = 23
my_new_car.update_odometer(23)
my_new_car.update_odometer(16)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_used_car = Car('Subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23000)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()