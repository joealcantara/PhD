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

class IceCreamStand(Restaurant):
    """ Modelling an ice cream stand """

    def __init__(self, restaurant_name, cuisine_type, *flavours):
        """ Initialise variables for Ice Cream Stand """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.flavours = flavours

    def menu(self):
        print("The ice cream flavours on offer are :")
        for flavour in self.flavours:
            print("\t" + flavour) 

test = Restaurant("'Nando's", "Chicken")
test.describe_restaurant()
test.restaurant_open()

test2 = Restaurant("KFC", "Chicken")
test3 = Restaurant("Carluccio's", "Italian")

test2.describe_restaurant()
test3.describe_restaurant()

test4 = IceCreamStand("Joe's", "Ice-Cream", "Vanilla", "Chocolate", "Raspberry")
test4.describe_restaurant()
test4.menu()