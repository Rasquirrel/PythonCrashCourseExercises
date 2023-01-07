
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

new_points = alien_0['points']

print('You just earned ' + str(new_points) + ' points!')

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)
print("\n\n\n")

alien_0 = {}
print(alien_0)

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

print("The alien's color is " + alien_0['color'] + ".")

# Changing the alien's color to yellow
alien_0['color'] = 'yellow'
print(alien_0)
print("Now the alien's color is " + alien_0['color'] + ".")

print("\n\n\n")


alien_0 = {'x_position': 0, 'y_position':25, 'speed': 'fast'}
print('Original x-position: ' + str(alien_0['x_position']) + '.')

# Move the alien to the right.
# Determines how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print('New x-position: ' + str(alien_0['x_position']) + '.')
