unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: {}".format(current_user))
    confirmed_users.append(current_user)

print('The following are confirmed users:')
for user in confirmed_users:
    print(user.title())
