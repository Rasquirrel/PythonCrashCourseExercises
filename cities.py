cities = {
    'sobral': {
        'size': 'medium',
        'country': 'brazil',
        'language': 'portuguese',
        'population': 210.711,
        'curiosity': "It's called 'North Little Princess'."
    },
    'vancouver': {
        'size': 'big',
        'country': 'canada',
        'language': 'english',
        'population': 675.218,
        'curiosity': "Vancouver has the 4th largest cruise ship terminal in the world."
    },
    'florence': {
        'size': 'medium',
        'country': 'italy',
        'language': 'italian',
        'population': 382.258,
        'curiosity' : "It was the birthplace of the Renaissance." 
    }
}

for citie, citie_info in cities.items():
    print("\nCity Name: " + citie.title())

    size = citie_info['size']
    country = citie_info['country']
    language = citie_info['language']
    population = citie_info['population']
    curiosity = citie_info['curiosity']

    print("\tSize: " + size + ';')
    print("\tCountry: " + country.title() + ';')
    print("\tLanguage: " + language.title() + ';')
    print("\tPopulation: " + str(population) + ';')
    print("\tCuriosity: " + curiosity + '.\n')
