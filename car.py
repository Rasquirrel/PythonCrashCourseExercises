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


'''
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.update_odometer(50)
my_new_car.increment_odometer(100)
my_new_car.read_odometer()
'''


class EletricCar(Car):
    """Trying to create a Eletric Car who is Car's child"""

    def __init__(self, make, model, year):
        """
        Initialize atributes of the parent class.
        Then initialize atributes specific to an eletric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 70
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


tesla = EletricCar('tesla', 'model s', 2016)
print(tesla.get_descriptive_name())
print(tesla.describe_battery())
print(tesla.fill_gas_tank())
