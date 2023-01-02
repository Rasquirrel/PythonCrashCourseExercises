
print('-' * 50)

guests = ['Emilly', 'Everton', 'Mom', 'Nazareno', 'João', 'Israel']

print(guests[0] + '! Would you like to come dinner with me? :)\n')

print('Hey ' + guests[1] + '! Would you like to come dinner with me?\n')

print(guests[2] + ', would you like to come dinner with me?\n')

print(guests[3] + ', would you like to come dinner with me?\n')

print(guests[4] + ', would you like to come dinner with me?\n')

print(guests[5] + ', would you like to come dinner with me?\n')

print('-' * 50)

print(guests[1] + " didn't come... Now I will invite Igor!\n")

print('-' * 50)

guests[1] = 'Igor'

print(guests[0] + '! Would you like to come dinner with me? :)\n')

print('Hey ' + guests[1] + '! Would you like to come dinner with me?\n')

print(guests[2] + ', would you like to come dinner with me?\n')

print(guests[3] + ', would you like to come dinner with me?\n')

print(guests[4] + ', would you like to come dinner with me?\n')

print(guests[5] + ', would you like to come dinner with me?\n')

print('-' * 50)
print('I found a bigger table! Now I will invite more three friends!')
print('-' * 50)

guests.insert(0, 'Rogério')
guests.insert(4, 'Enzo')
guests.append('Marcelo')

print(guests[1] + '! Would you like to come dinner with me? :)\n')

print('Hey ' + guests[0] + '! Would you like to come dinner with me?\n')

print(guests[2] + ', would you like to come dinner with me?\n')

print(guests[3] + ', would you like to come dinner with me?\n')

print(guests[4] + ', would you like to come dinner with me?\n')

print(guests[5] + ', would you like to come dinner with me?\n')

print(guests[6] + ', would you like to come dinner with me?\n')

print(guests[7] + ', would you like to come dinner with me?\n')

print(guests[8] + ', would you like to come dinner with me?\n')

print('-' * 50)
print('I found out that I cannot invite everyone, just two of them...')
print('-' * 50)

first = guests.pop(0)
print('Sorry ' + first + ". I don't will invite you this time.")

third = guests.pop(2)
print('Sorry ' + third + ". I don't will invite you this time.")

fourth = guests.pop(3)
print('Sorry ' + fourth + ". I don't will invite you this time.")

sixth = guests.pop(5)
print('Sorry ' + sixth + ". I don't will invite you this time.")
print(guests)

seventh = guests.pop(1)
print('Sorry ' + seventh + ". I don't will invite you this time.")

eigth = guests.pop(2)
print('Sorry ' + eigth + ". I don't will invite you this time.")

israel = guests.pop(2)
print('Sorry ' + israel + ". I don't will invite you this time.")
print('-' * 50)

print('Hey ' + guests[0] + ' and ' + guests[1] + '!')
print('You are still invited for the dinner!')

print('-' * 50)

del guests[0]
del guests[0]

print(guests)
