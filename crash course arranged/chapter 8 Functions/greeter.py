def greet_user():
    '''Display simple greeting'''
    print('Hello!')

greet_user()

'''passing information to a function'''
def greet_user(username):

    '''greeting with the user's name'''
    print('Hello, {}!'.format(username.title()))

greet_user('stella')

