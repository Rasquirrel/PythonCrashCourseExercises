pizzas = ['mussarela', 'calabresa', 'carne de sol']
friend_pizzas = pizzas[:]

friend_pizzas.append('bacon')

print("My favorite pizzas are: ")
for pizza in pizzas:
    print(pizza.title())

print("\nMy friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza.title())
