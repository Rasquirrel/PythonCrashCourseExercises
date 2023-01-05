avaliable_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple',
                      'extra cheese']

requested_toppings = ['mushrooms', 'olives', 'corns']

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in avaliable_toppings:
            print('Adding ' + requested_topping + '...' )
        else:
            print('Sorry, we are out of ' + requested_topping + '. :(')

    print('Finished making your pizza!')
else:
    print('Are you sure you want a plain pizza?')

