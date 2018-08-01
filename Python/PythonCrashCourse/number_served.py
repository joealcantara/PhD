class Restaurant():
    """ First attempt to model a restaurant """

    def __init__(self, restaurant_name, cuisine_type):
        """ Initialise variables for Restaurant """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.num_served = 0

    def describe_restaurant(self):
        """ Describes the restaurant """
        print("Restaurant Name : " + self.restaurant_name)
        print("Cuisine Type : " + self.cuisine_type)
        print("Number Served :" + str(self.num_served))

    def restaurant_open(self):
        """ Signals that the restaurant is open """
        print("The " + self.restaurant_name + " restaurant is now open for business")
    
    def number_served(self, num_served):
        """ Adds number of customers served variable """
        self.num_served = num_served

    def increment_served(self, increment):
        self.num_served += increment


test = Restaurant("'Nando's", "Chicken")
test.describe_restaurant()
test.restaurant_open()

test2 = Restaurant("KFC", "Chicken")
test3 = Restaurant("Carluccio's", "Italian")

test2.describe_restaurant()
test3.describe_restaurant()

test.number_served(100)
test.describe_restaurant()
test.increment_served(100)
test.describe_restaurant()