def city_country(city, country):
    output = '"' + city.title() + ", " + country.title() + '"'
    return output

print(city_country('santiago', 'chile'))
print(city_country('london', 'england'))
print(city_country('paris', 'france'))