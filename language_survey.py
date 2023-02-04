from survey import AnonymousSurvey

# Define a question and mark the survey
question = 'What language did you first learn to speak?'
my_survey = AnonymousSurvey(question)

my_survey.show_question()

print('Enter "q" at any time to quit. \n')

while True:
    response = input('Language: ')
    if response == "q": break
    my_survey.store_response(response)

# Show the results of the survey
print('\nThank you to everyone who participated in the survey!')
my_survey.show_results()

