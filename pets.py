def describe_pet(animal_type, pet_name):
    """Display informations about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('cat', 'dina')
describe_pet('cat', 'newton')
describe_pet('parrot', 'willam')
print()
# Keyword Arguments:

describe_pet(animal_type='cat', pet_name='dina')
describe_pet(pet_name='belu', animal_type='dog')
describe_pet(animal_type='dog', pet_name='theo')
