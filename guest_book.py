file_name = 'guest_book.txt'

print('Enter "quit" when you want to stop it.\n')

while True:
    name = input('What is your name? ')

    if name == 'quit': break

    print('Welcome ' + name.title() + '!')
    print('Recording your visit...\n')

    with open(file_name,'a') as file_object:
        file_object.write(name.title() + '\n')

