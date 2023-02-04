print('This program will sum two numbers.')
print('Enter "q" to exit.')

active = True

while active:
    first_number = input('Enter the first number: ')
    if first_number == 'q': break

    second_number = input('Enter the second number: ')
    if second_number == 'q': break

    try:
        sum = int(first_number) + int(second_number)
    except ValueError:
        print('Please, insert a numerical value!!!')
    else:
        print('The result is: ' + str(sum))

