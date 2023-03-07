cars = ['bmw', 'audi', 'toyota', 'subaru']
'''sorting a list alphabetically'''
cars.sort()
print(cars)

'''sorting a list in reverse'''
cars.sort(reverse=True)
print(cars) #the order is permanently changed


'''sorting a list temporarily'''
cars = ['bmw', 'audi', 'toyota', 'subaru']

'''print the orginal list'''
print('Here is the original list: {}'.format(cars))

'''Print the sorted list'''
print('Here is the sorted list: {}'.format(sorted(cars)))

'''the original list again'''
print('Here is the original list: {}'.format(cars))

'''print list in reverse order'''
cars.reverse()
print(cars)

'''finding the length of a list'''
print(len(cars))
