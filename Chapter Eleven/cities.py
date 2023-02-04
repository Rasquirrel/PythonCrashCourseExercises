"""
This module have a function that
prints a formatted city name
"""

def city_name(city: str, country: str, population_count=''):
    """
    Receive City and Country names then return a formatted name
    """
    city_name = city
    country_name = country

    if population_count:
        popult = population_count
        pop_str = str(popult)
        formatted = city.title() + ", " + country.title() + " population - " + pop_str

    else:
        formatted = city.title() + ", " + country.title()

    return formatted

