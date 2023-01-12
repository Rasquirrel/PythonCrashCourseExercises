def city_country(city, country):
    phrase = '"' + city.title() + ', ' + country.title() + '"'

    return phrase

sobral = city_country('sobral', 'brasil')
las_vegas = city_country(country='United States',
 city='las vegas')
moscow= city_country('moscow', 'russia')

print(sobral)
print(las_vegas)
print(moscow)
