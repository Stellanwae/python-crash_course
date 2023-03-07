dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

'''tuples cannot be changed
you cannot do this:
dimensions[0] = 250''' 


'''A tuple with a single number'''
my_t = (3,)

'''Looping through a tuple'''
print('These are looped dimensions')
for d in dimensions:
    print(d)

'''writing over a tuple'''
print('Original dimension:')
print(dimensions)

'''new dimension'''
dimensions = (400, 100)
print(dimensions)