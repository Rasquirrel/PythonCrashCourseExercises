favorite_places = {
    'john': ['alaska', 'nebraska', 'egypt'],
    'loremipsilum': ['france', 'italy', 'florence'],
    'joe': ['africa', 'arabia', 'pakistan']
}

print("Peoples and their favorite places: \n")

for people, places in favorite_places.items():

    print("\tName: " + people.title() + ';')
    print("\tFavorite Places: ")
    for place in places:
        print("\t\t" + place.title() + ".")
    print("\n")
