topping = ''

while topping != 'quit':
    topping = input("Please, enter the name of the pizza topping: ")
    if topping == 'quit':
        break
    else:
        print("Adding " + topping + ".")
        print("Enter 'quit' when you want to stop")
