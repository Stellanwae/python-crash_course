motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

'''Changing the value of index one'''
motorcycles[0] = 'ducati'
print(motorcycles)

'''adding elements to a list'''
motorcycles.append('honda')
print(motorcycles)

'''adding more'''
motorcycles.append('yamaha')
motorcycles.append('suzuki')

'''Inserting an element to a list'''
motorcycles.insert(0,'BMW')
print(motorcycles)

'''Removing elements from a list'''
del motorcycles[0]
print(motorcycles)
del motorcycles[1]
print(motorcycles)

'''Using the pop method
Pop prints the value on the right side of the list
then it deletes it
'''

motorcycles.pop()
'''to get the value popped without specifying position'''
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print("{} is the popped motorcycle".format(popped_motorcycle))

'''Popping from a specific position'''
motorcycles.pop(1)
popped_motorcycle = motorcycles.pop(1)
print("{} is the popped motorcycle".format(popped_motorcycle))
print(motorcycles)

'''Removing item by value
using remove()'''
motorcycles.remove("ducati")
print(motorcycles)
