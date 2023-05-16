def send_messages():
    short_messages = ['Hello', 'How are you', 'What is your list']
    for message in  short_messages:
        print(message)
    sent_messages = []
    while short_messages:
        message = short_messages.pop()
        sent_messages.append(message)
    print('These are sent messages:')
    for message in sent_messages:
        print(message)

send_messages()

