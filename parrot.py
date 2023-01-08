prompt = "Please, tell me something and I will repeat it back to you.\n"
prompt += 'Enter "quit" when you want to leave: '

message = ''

while message != 'quit':
    message = input(prompt)
    
    if message != 'quit':
        print(message + '\n')
