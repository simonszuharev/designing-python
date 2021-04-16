class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 1
        self.question_list = q_list
        self.user_score = 0

    def next_question(self):
        the_question = self.question_list[self.question_number - 1]
        user_input = input(f"{self.question_number}) {the_question.text} (True/False)? ")
        self.check_answer(user_input, the_question.answer)
        self.question_number += 1

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer:
            print("You got it right! The right answer is ", correct_answer)
            self.user_score += 1
        else:
            print("You got it wrong! The right answer is ", correct_answer)
        print("Your current score is", self.user_score, "out of 12\n")
