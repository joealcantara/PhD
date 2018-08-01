class Restaurant():
    """ First attempt to model a restaurant """

    def __init__(self, restaurant_name, cuisine_type):
        """ Initialise variables for Restaurant """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """ Describes the restaurant """
        print("Restaurant Name : " + self.restaurant_name)
        print("Cuisine Type : " + self.cuisine_type)

    def restaurant_open(self):
        """ Signals that the restaurant is open """
        print("The " + self.restaurant_name + " restaurant is now open for business")

test = Restaurant("'Nando's", "Chicken")
test.describe_restaurant()
test.restaurant_open()

test2 = Restaurant("KFC", "Chicken")
test3 = Restaurant("Carluccio's", "Italian")

test2.describe_restaurant()
test3.describe_restaurant()