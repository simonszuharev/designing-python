from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Comic Sans MS", 25, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("Blue")
        self.goto(0, 270)
        self.update_score_screen()

    def __update_the_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def __add_score(self):
        self.score += 1
        self.clear()
        self.update_score_screen()

    def __loser(self):
        self.goto(0, 0)
        self.color("blue")
        self.write("GAME OVER", align=ALIGNMENT, font=("Comic Sans MS", 40, "bold"))

    def add(self):
        self.__add_score()

    def update_score_screen(self):
        self.__update_the_score()

    def game_over(self):
        self.__loser()
