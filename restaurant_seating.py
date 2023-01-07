prompt = "Goodnight, and welcome to our restaurant!"
prompt += "\nPlease, tell me, how many people are in your dinner group? "


quantity = input(prompt)
quantity = int(quantity)

if quantity > 8:
    print("Well, I see that you have a pretty large group.")
    print("You will need to wait for a table.")
else:
    print("Your table is ready!")
