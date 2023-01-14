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

print(my_restaurant.name)
print(my_restaurant.cuisine_type)

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
