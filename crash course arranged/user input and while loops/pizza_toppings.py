prompt = 'Enter your series of pizza toppings.'
prompt += 'Enter \'quit\' to stop'


while True:
    message = input(prompt)
    if message != 'quit':
        print(message)
        print('Adding {} to your pizza'.format(message))
    else:
        break