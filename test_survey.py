import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

    def test_store_single_response(self):
        """Tests that a single response is stored properly."""
        question = 'What language did you learn first? '
        my_survey = AnonymousSurvey(question)
        response = 'English'
        my_survey.store_response(response)

        self.assertIn(response, my_survey.responses)

    def test_store_three_responses(self):
        """Test that three invidual responses are stored properly"""
        question = 'What language did you learn first?'
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Portuguese', 'Russian']

        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)

    
unittest.main()

