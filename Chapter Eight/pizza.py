def make_pizza(size, *toppings):
    """This function prints the list of topping that have been requested"""
    print("Making a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print('\t' + topping + ';')
