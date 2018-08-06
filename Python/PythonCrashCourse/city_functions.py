def city(city, country, population=''):
    """ Takes city and country and outputs this neatly """
    if population:
        fullString = city.title() + ", " + country.title() + " - " + str(population)
    else:
        fullString = city.title() + ", " + country.title()
    return fullString
