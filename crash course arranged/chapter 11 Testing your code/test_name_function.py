import unittest
from name_function import get_formatted_name

class TestNameFunction(unittest.TestCase):
    def test_formatted_name(self):

        formatted_name = get_formatted_name('Aaron', 'Moses')
        self.assertEqual(formatted_name, 'Aaron Moses')

if __name__ == '__main__':
    unittest.main()

