try:
    import unittest
    from this import myfunction
    class TestMe(unittest.TestCase):
        
        def testfunction(self):
            test = myfucntion("arg1", "arg2")
            self.assertEqual(test, "the expected answer")

    if __name__ == '__main__':
        unittest.main()
except ImportError:
    print('There seems to be a problem with your import files')