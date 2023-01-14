class Restaurant:
    """This class will simulate the building of a restaurant"""

    def __init__(self, name, cuisine_type):
        """
        Initial method to acquire the firsts two attributes:
        name: The restaurant name
        cuisine_type: The restaurant's cuisine type.
        """
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant's name: " + self.name.title() + ';')
        print("Restaurant's cuisine type: " + self.cuisine_type.title() + '.')

    def open_restaurant(self):
        print("Opening " + self.name.title() + "!")


my_restaurant = Restaurant("isac cooks - restaurant", 'brazilian cuisine')
void_restaurant = Restaurant('void plateau', 'space cuisine')
shing_shong_restaurant = Restaurant('kashjdqkw sjda', 'chinese cuisine')

my_restaurant.describe_restaurant()
print()

void_restaurant.describe_restaurant()
print()

shing_shong_restaurant.describe_restaurant()
print()
