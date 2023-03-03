'''Lists
'''
bicycles = ['trek', 'cannondale','redline', 'specialised']
print(bicycles)

'''accessing elements in a list'''

print(bicycles[0])
print(bicycles[0].title())

'''accessing every member in the list now'''
print(bicycles[0].title())
print(bicycles[1].title())
print(bicycles[2])
print(bicycles[3])

'''accessing the last element'''
print(bicycles[-1])

'''using individual values from a list'''
message = "My favourite bicyle is {}".format(bicycles[0])
print(message)