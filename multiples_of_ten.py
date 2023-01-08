# This program will ask the user a number, and then tell if
# it's a multiple of 10 or not.

prompt = "Enter a number, and I will tell you if it's\n"
prompt += "a multiple of 10 or not: \n"

number = input(prompt)
number = int(number)

if number % 10 == 0:
    print("\nThe number  " + str(number) + " is multiple of 10.")
else:
    print("\nThe number " + str(number) + " isn't multiple of 10.")
