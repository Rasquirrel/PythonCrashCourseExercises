cars = ['bmw', 'audi', 'toyota', 'subaru']
#cars.sort() # Sort in alphabetical order, and I can never revert it.
			# It changes the list order permanently.
#print(cars)

#cars.sort(reverse = True) # The diferrence is that now it is backwards.
#print(cars)

# To sort a list temporarily we uses the sorted(list_name) method.
# this funcion also acepts a reverse = True.

print('This is my list: ')
print(cars)

print('Now my list is sorted!')
print(sorted(cars))

print('But my original list stills in the same order!')
print(cars)

# To reverse the order of the elements of a list, we use the reverse() method
# This just reverse the order, not sort alphabeticaly.
# It changes the order permanently but I can fix by just applying the method again in the same
# list.

print('This is my list: ')
print(cars)

print('Now, this is my list in reverse order: ')
cars.reverse()
print(cars)

# To findout the length of a list, we use the len() method

print('The length of the cars list is: '+ str(len(cars)) + ' itens.')
