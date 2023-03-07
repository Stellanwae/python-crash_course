places = ['new york', 'cairo', 'madagascar', 'israel', 'rwanda']

'''list in original order'''
print('This is the original list: {}'.format(places))

'''temporarily in alphabetical order
list not tampered with'''
print('The sorted list: {}'.format(sorted(places)))

'''confirming if original is not tampered with'''
print('this is the original: {}'.format(places))

'''using sorted to print the reverse'''
print('This is sorted in reverse: {}'.format(sorted(places, reverse=True)))

'''show still in original order'''
print(places)

'''user reverse to order list
'''
places.reverse()
print(places)

'''back to original using reverse'''
places.reverse()
print(places)

'''using sort() to arrange alphabetically'''
places.sort()
print(places)

'''reverse order'''
places.sort(reverse=True)
print(places)



