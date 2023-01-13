def make_pizza(*toppings):
    """This function prints the list of topping that have been requested"""
    print("Making a pizza with the followind toppings: ")
    for topping in toppings:
        print('\t' + topping + ';')


make_pizza('cheese')
make_pizza('onions', 'peppers', 'mushrooms')
