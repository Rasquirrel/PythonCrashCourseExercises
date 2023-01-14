
price = 0

while True:
    age = (input("Please enter your age: \n" +
    "(Enter 'quit' if you want to exit.)"))

    if age == 'quit':
        break

    else:
        age = int(age)
    
        if age < 3:
            print("Because you have " + str(age) +
            ", you dont have to pay.")
        
            break
        
        elif age > 3 and age < 12: 
            price = 10
            print("Because you have " + str(age) +
            ", you have to pay: $" + str(price) + '.')

            break
        
        elif age > 12:
            price = 15
            rint("Because you have " + str(age) +
            ", you have to pay: $" + str(price) + '.')

            break

print("Enjoy!")
