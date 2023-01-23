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


class IceCreamStand(Restaurant):
    """This class will create a IceCreamstand!"""

    def __init__(self, name, cuisine_type):
        """
        Initialize methods and attributes from the parent class.
        Then initialize an attribute specif to the ice cream stand.
        """
        super().__init__(name, cuisine_type)
        flavours = ['chocolate', 'coconut', 'orange', 'berry']
    
    def show_flavours():
        """Prints all the avaliable flavours"""
        print()



