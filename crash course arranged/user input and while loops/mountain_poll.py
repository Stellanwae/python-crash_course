'''filling in a dictionary with user input'''
polling_active = True
polling_responses = {}
while polling_active:
    name = input('what is your name?')
    response = input('what is your response?')
    repeat = input('should we repeat the poll?')
    polling_responses[name] = response
    if repeat == 'no':
        polling_active = False
        

print(polling_responses)   