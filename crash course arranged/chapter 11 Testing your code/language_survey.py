from survey import AnonymousSurvey
'''Define question
'''
question = 'What is the language you first spoke?'

while True:
    ask = input(question)
    print('Language: {}'.format(ask))
    if ask == 'q':
        break
