dina = {
    'name': 'dina',
    'type': 'cat',
    'fur_color': 'white with brown',
    'eyes_color': 'blue',
    'size': 'medium',
    'race': 'mixed'
}

newton = {
    'name': 'newton',
    'type': 'cat',
    'fur_color': 'white and black',
    'eyes_color': 'yellow',
    'size': 'small',
    'race': 'mixed'
}

xane = {
    'name': 'xane',
    'type': 'cat',
    'fur_color': 'brown with white',
    'eyes_color': 'blue',
    'size': 'medium',
    'race': 'mixed'
}

pets = [dina, newton, xane]

print("My pets: \n")

for pet in pets:
    pet_name = pet['name']
    pet_type = pet['type']
    fur_color = pet['fur_color']
    eyes_color = pet['eyes_color']
    size = pet['size']
    race = pet['race']

    print("\tName: " + pet_name.title() + ';')
    print("\tType: " + pet_type + ';')
    print("\tFur Color: " + fur_color + ';')
    print("\tEyes Color: " + eyes_color + ';')
    print("\tSize: " + size + ';')
    print("\tRace: " + race + ';\n')
