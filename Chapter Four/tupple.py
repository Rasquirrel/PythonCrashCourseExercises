# Tupples are like lists, but they don't let you change individual values.
# You can change the values if you reasign the variable of the tupple.

cats = ('dina', 'newton', 'xane', 'miranga', 'tina', 'leleca')

print("These are the names of all the cats that I know: ")
for cat_name in cats:
    print(cat_name.title())

print("\nThis is the list:")
print(cats)
print()

print("Now this is the sorted list:")
print(sorted(cats))
print()

print("This is the reversal list:")
print(sorted(cats, reverse = True))

print('These are the first three cats from the list: ')

print(cats[:3])

print("Starting from the third and going to the fifth: ")
print(cats[2:6])

print("Printing the last 2 cats: ")
print(cats[-2:])

print("Now I will copy the tupple to an list. ")
cats_list = list(cats[:])

print('This is the tupple: ')
print(cats)
print()

print('This is the list: ')
print(cats_list)
print()
