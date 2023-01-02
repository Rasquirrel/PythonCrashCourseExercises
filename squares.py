squares = []

for number in range(1, 11):
    square = number ** 2
    squares.append(square)
print('This is my list of numbers: ')
print(squares)

# minimal value of the list: min(list_name)
print('The minimal value of this list is: ' + str(min(squares)))
# max value of the list: max(list_name)
print('The max value of this list is: ' + str(max(squares)))
# sum of the values of the list: sum(list_name)
print('The sum of all the values of this list is: ' + str(sum(squares)))

# I can create the same list with a more compact code. List Comprehensions.
squares_compact = [number ** 2 for number in range(1,11)]

print(squares_compact)
