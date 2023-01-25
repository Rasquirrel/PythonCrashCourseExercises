filename = 'programming_poll.txt'

while True: 
    with open(filename, 'a') as file_object:
       print('(Enter "q" when you want to stop)')
       name = input("What's your name? ")

       if name == 'q': break

       why = input("Why do you like programming? ")

       if why == 'q': break

       print('\nWriting on "' + filename + '"...')
       file_object.write(name.title() + "'s reason: " + why.capitalize() + ';\n')

