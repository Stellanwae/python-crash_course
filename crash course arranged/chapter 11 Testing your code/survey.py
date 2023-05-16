class AnonymousSurvey:
    def __init__(self, question):
        '''Store a question to prepare for a survey'''
        self.question = question
        self.responses = []
    
    def show_question(self):
        '''Show the questions needed in the survey'''
        print("{}".format(self.question))
    
    def store_response(self, new_response):
        '''storing response in list'''
        self.responses.append(new_response)
    
    def show_results(self):
        '''show all the results in the list'''
        for response in self.responses:
            print('- {}'.format(response))