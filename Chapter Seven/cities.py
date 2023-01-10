prompt = "Please, enter the name of a city you alrady visited.\n"
prompt += "(Enter 'quit' when you want to exit.): "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!\n")
