favorite_numbers = {
                   'mae': [2, 4, 5, 6],
                   'isac': [4, 9, 13, 8],
                   'john': [1, 2, 3, 99],
                   'doe' : [999, 10, 20 ,30],
                   'dina': [4, 9, 13, 8]
                  }

for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + "'s favorite numbers are: ")
    for number in numbers:
        print("\t" + str(number) + ";")
print('\n')
