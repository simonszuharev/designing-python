from turtle import Turtle

ALIGNMENT = "left"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("Blue")
        self.goto(-280, 270)
        self.update_score_screen()

    def __update_the_score(self):
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def __add_level(self):
        self.level += 1
        self.clear()
        self.update_score_screen()

    def __loser(self):
        self.goto(0, 0)
        self.color("blue")
        self.write("GAME OVER", align="center", font=("Comic Sans MS", 40, "bold"))

    def add(self):
        self.__add_level()

    def update_score_screen(self):
        self.__update_the_score()

    def game_over(self):
        self.__loser()
