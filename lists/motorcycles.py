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

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print("{} is too expensive for me".format(too_expensive.title()))

'''The remove() method only deletes the first occurence of the value
you specify. if there's a possibility the occurence appears more than
once in this list, you'll need to use a loop to make all occurences of the value are 
removed. More on that coming up'''