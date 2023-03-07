'''guest list'''
guests = ['holmes', 'john', 'walker', 'martha', 'simeon', 'mahanaim']

'''remove guests using pop till only two remain
store in variable to enable access'''
message0 = guests.pop()
message1 = guests.pop()
message2 = guests.pop()
message3 = guests.pop()

print(guests)

'''message from those who won't come'''
print('{}, I hope you find time next time'.format(message0.title()))
print('{}, I hope you find time next time'.format(message1.title()))
print('{}, I hope you find time next time'.format(message2.title()))
print('{}, I hope you find time next time'.format(message3.title()))

'''using del to remove the last two persons
remains empty list'''

del guests[0]
del guests[0]

print(guests)