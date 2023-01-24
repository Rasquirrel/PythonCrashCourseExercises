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
        self.number_served = 0

    def describe_restaurant(self):
        print("Restaurant's name: " + self.name.title() + ';')
        print("Restaurant's cuisine type: " + self.cuisine_type.title() + '.')

    def open_restaurant(self):
        print("Opening " + self.name.title() + "!")

    def set_number_served(self, quant: int):
        """Changes the number of customers who were served"""
        self.number_served = quant

    def increment_number_served(self, number: int):
        """Increments the number of customers who were served"""
        if number < 0:
            print("Hey, you can't increment a negative number!")
        else:
            self.number_served += number


my_restaurant = Restaurant("isac cooks - restaurant", 'brazilian cuisine')
void_restaurant = Restaurant('void plateau', 'space cuisine')
shing_shong_restaurant = Restaurant('kashjdqkw sjda', 'chinese cuisine')

my_restaurant.number_served = 15
print(my_restaurant.number_served)

my_restaurant.set_number_served(20)
print(my_restaurant.number_served)

my_restaurant.increment_number_served(10)
print(my_restaurant.number_served)
