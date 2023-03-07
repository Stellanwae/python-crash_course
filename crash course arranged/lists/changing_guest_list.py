'''a list of guests'''
guests = ['john', 'martha', 'mary', 'luke', 'simeon']

'''removing guests who can't come '''
not_come = guests.pop(2)
not_come1 = guests.pop(2)
'''printing guests'''
print(guests)

'''printing a message stating the name of those who wont come'''
print('{} will not be able to come'.format(not_come.title()))
print('{} will not be able to come'.format(not_come1.title()))

'''second invitation'''
print('Hello {}, you are invited to this dinner'.format(guests[0]))
print('Hello {}, you are invited to this dinner'.format(guests[1]))
print('Hello {}, you are invited to this dinner'.format(guests[2]))

'''replacing the guests using the insert method'''
guests.insert(0, 'holmes')
guests.insert(2, 'walker')
guests.append('mahanaim')
'''more guests'''
print('Hello {}, welcome to the party.'.format(guests[0].title()))
print('Hello {}, welcome to the party.'.format(guests[1].title()))
print('Hello {}, welcome to the party.'.format(guests[2].title()))
print('Hello {}, welcome to the party.'.format(guests[3].title()))
print('Hello {}, welcome to the party.'.format(guests[4].title()))
print('Hello {}, welcome to the party.'.format(guests[5].title()))

print(guests)