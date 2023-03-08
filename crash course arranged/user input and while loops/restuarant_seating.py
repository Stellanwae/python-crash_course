'''ask for number of people in a dinner group'''
seating = input('How many people are coming to this dinner group? ')

'''make it an int'''
seating = int(seating)

'''conditions'''
if seating > 8:
    print('You will have to wait for a table')
else:
    print('Table is ready')
