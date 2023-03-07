magicians = ['alice', 'david', 'carolina']

'''looping through a list'''
for magician in magicians:
    print(magician.title())

'''doing more in a loop'''
for magician in magicians:
    print('{}, that was a great trick'.format(magician.title()))
    print('I can\'t wait for your next trick\n'.format(magician.title()))

'''doing something after a loop'''
print('Thank you everyone. That was a nice trick')