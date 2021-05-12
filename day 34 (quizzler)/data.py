import requests


class QuestionsData:

    def __init__(self):
        self.response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
        self.response.raise_for_status()
        self.question_data = self.response.json()

    def get_data(self):
        questions_dict = self.question_data['results']

        return questions_dict
