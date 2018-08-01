def make_car(manufacturer, make, **attributes):
    """ Builds the profile of a car """
    car = {}
    car['manufacturer'] = manufacturer
    car['make'] = make
    for k, v in attributes.items():
        car[k] = v
    return car

car = make_car("subaru", "outback", color = 'blue', tow_package = True)
print(car)