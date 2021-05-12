from data import QuestionsData
from quiz_brain import QuizBrain
from ui import QuizzInterface

qd = QuestionsData()
qd_list = qd.get_data()
question_bank = []

quiz = QuizBrain(question_bank)
quiz_ui = QuizzInterface(quiz)

