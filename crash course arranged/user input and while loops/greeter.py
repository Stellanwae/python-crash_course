name = input('Please enter your name: ')
print('Hello, {}!'.format(name))

'''putting the message in a prompt'''
prompt = 'If you tell us who you are, we can personalise the messages you see.'
prompt += '\What is your first name? '

name = input(prompt)
print('Hello {}'.format(name))