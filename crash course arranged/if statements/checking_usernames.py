user_name = ['martha', 'mary', 'admin', 'james', 'dorcas']
current_users = ['holmes', 'mary', 'june', 'james', 'dorcas']

for name in user_name:
    if name in current_users:
        print('User name is available')
    else:
        print('Need to add a new user name')