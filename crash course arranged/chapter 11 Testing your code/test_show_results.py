import unittest
from survey import AnonymousSurvey

class TestShowResults(unittest.TestCase):
    '''testing using a method'''
    def test_show_results(self):
        question = 'What is your first language? '
        survey = AnonymousSurvey(question)
        store_response = survey.store_response("english")
        show_results = survey.show_results()
        self.assertEqual("Survey results:\n- english", show_results)
        
if __name__ == "__main__":
    unittest.main()