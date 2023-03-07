cities = ['nairobi', 'cairo', 'kigali', 'addis ababa', 'kampala', 'khartoum', 'paris']

'''puting title case'''
print(cities[0].title())

'''adding elements'''
cities.append('london')

print(cities)

'''inserting'''
cities.insert(0, 'lagos')
print(cities)

'''removing elements'''

del cities[0]
print(cities)

cities.pop()
print(cities)

cities.pop(3)
print(cities)

cities.remove('khartoum')
print(cities)

'''sorting'''

'''permanent sorting'''
cities.sort()
print('This is permanently sorted: ')
print(cities)

'''reverse permanent sorting'''
cities.sort(reverse=True)
print('This is permanent reverse sorting: ')
print(cities)

'''temporary sorting'''
cities = ['nairobi', 'cairo', 'kigali', 'addis ababa', 'kampala', 'khartoum', 'paris']


print('This is temporary sorting')
print(sorted(cities))

'''reverse temporary sorting'''
print('This is temporary sorting {}'.format(sorted(cities, reverse=True)))
