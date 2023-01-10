def describe_pet(animal_type, pet_name):
    """Display informations about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('cat', 'dina')
describe_pet('cat', 'newton')
describe_pet('parrot', 'willam')
