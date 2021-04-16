from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []


for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    q_model = Question(question_text, question_answer)
    question_bank.append(q_model)

quiz = QuizBrain(question_bank)

for i in question_bank:
    quiz.next_question()

print("Congrats! Your final score is", quiz.user_score,"!!! Congrats!!!")
