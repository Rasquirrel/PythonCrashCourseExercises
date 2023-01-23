import car

uno = car.EletricCar('a5', 'fiat', 2010)
print(uno.get_descriptive_name())
uno.battery.describe_battery()

audi = car.Car('audi', '5e', 2018)
audi.read_odometer()
print(audi.get_descriptive_name())
