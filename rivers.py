rivers = {'amazon river': 'brazil',
          'yangtze river': 'china',
          'nile': 'egypt'
         }

for river, country in sorted(rivers.items()):
    print("The " + river.title() + " is located in " + country.title() + ".")

print("\nThese are the countrys: ")

for country in sorted(rivers.values()):
    print(country.title())

print("\nAnd these are the rivers: ")

for river in sorted(rivers.keys()):
    print(river.title())
