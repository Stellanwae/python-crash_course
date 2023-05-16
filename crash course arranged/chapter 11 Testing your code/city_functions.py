def location(city, country, population=int()):
    '''return simple string of city and country'''
    return "{}, {} - population {}".format(city, country, population)
plocation = location('Nairobi', 'Kenya')
print(plocation)