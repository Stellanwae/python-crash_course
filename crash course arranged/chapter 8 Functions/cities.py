def describe_city(city, country='kenya'):
    print('{} is in {}'.format(city.title(), country.title()))

'''calling for the city'''
describe_city('nairobi')
'''another'''
describe_city('kisumu')
'''not the default country'''
describe_city('kigali', 'rwanda')