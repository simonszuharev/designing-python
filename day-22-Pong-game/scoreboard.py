from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Comic Sans MS", 80, "normal")


class ScoreBoard(Turtle):

    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x_cor, y_cor)
        self.update_score_screen()

    def __update_the_score(self):
        self.write(self.score, align=ALIGNMENT, font=FONT)

    def __add_score(self):
        self.score += 1
        self.clear()
        self.update_score_screen()

    def add(self):
        self.__add_score()

    def update_score_screen(self):
        self.__update_the_score()
