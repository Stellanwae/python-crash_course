'''passing a list'''
def greet_users(names):
    for name in names:
        print('Hello, {}!'.format(name.title))


user_names = ['Hannh', 'Ty', 'Margot']
greet_users(user_names)