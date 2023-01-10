dream_vacations = {}

poll_active = True

while poll_active:
    name = input("Hello! What's your name? ")
    place = input("So, if you could travel to a nice place, where you would like to go? ")

    dream_vacations[name] = place

    next = input("Ok, thank you! Would you like to let another people response? (yes/no) ")

    if next == 'no':
        poll_active = False

print("\n-- Closed Poll --\n")

for name, place in dream_vacations.items():
    print(name.title() + " would like to travel to " + place.title() + ".")
