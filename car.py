class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print('This car has ' + str(self.odometer_reading) + ' miles on it')

    def update_odometer(self, mileage: int):
        """Set the odometer reading to the given value"""
        if mileage <= self.odometer_reading:
            print('Hey, you can not rollback a odometer!')
        else:
            self.odometer_reading = mileage

    def increment_odometer(self, miles):
        """Add the given value to the odometer reading"""
        self.odometer_reading += miles
    
    def fill_gas_tank(self):
        """Fill the gas tank"""
        print('Filling the gas tank...')


class Battery():
    """A simple attempt to model a battery for an eletric car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

        

class EletricCar(Car):
    """Trying to create a Eletric Car who is Car's child"""

    def __init__(self, make, model, year):
        """
        Initialize atributes of the parent class.
        Then initialize atributes specific to an eletric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
    
    
    def fill_gas_tank(self):
        """Eletric cars doesn't have a gas tank!"""
        print("This car doesn't need a gas tank!")


tesla = EletricCar('tesla', 'model s', 2016)
print(tesla.get_descriptive_name())
tesla.battery.describe_battery()
tesla.fill_gas_tank()
tesla.battery.get_range()
