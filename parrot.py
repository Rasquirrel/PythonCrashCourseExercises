prompt = "Please, tell me something and I will repeat it back to you.\n"
prompt += 'Enter "quit" when you want to leave: '

active = True

while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)
