import unittest
from city_functions import location

class Testlocation(unittest.TestCase):

    '''method to test city'''
    def test_city(self):
        '''store test function in variable'''
        function_var = location("Nairobi", "Kenya")
        self.assertEqual(function_var, 'Nairobi, Kenya - population 0')

if __name__ == '__main__':
    unittest.main()