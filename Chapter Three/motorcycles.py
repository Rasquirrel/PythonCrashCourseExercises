motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('suzuki')
print(motorcycles)

too_expensive = motorcycles[2]
motorcycles.remove(too_expensive)
print(motorcycles)
print('\n A ' + too_expensive.title() + ' is too expensive for me.')
