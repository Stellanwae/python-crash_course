user_name = ['martha', 'mary', 'admin', 'james', 'dorcas']

for name in user_name:
    if name == 'admin':
        print('Hello {}, would like to see a status report?'.format(name.title()))
    else:
        print('Hello {}, thank you for logging in again'.format(name.title()))
