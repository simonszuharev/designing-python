from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
TRUE = "True"
FALSE = "False"


class QuizzInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="whatever", fill=THEME_COLOR, font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_pic = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_pic, highlightthickness=0, command=self.true_button)
        self.true_button.grid(row=2, column=0)

        false_pic = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_pic, highlightthickness=0, command=self.false_button)
        self.false_button.grid(row=2, column=1)
        self.next_q()

        self.window.mainloop()

    def next_q(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.canvas.config(bg="white")
        else:
            self.canvas.itemconfig(self.question_text, text="END OF THE GAME!")
            self.canvas.config(bg="white")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_button(self):
        self.feedback(self.quiz.check_answer(TRUE))

    def false_button(self):
        self.feedback(self.quiz.check_answer(FALSE))

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_q)
