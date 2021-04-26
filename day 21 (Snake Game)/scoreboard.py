from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Comic Sans MS", 25, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.color("Blue")
        self.goto(0, 270)
        self.update_score_screen()

    def __update_the_score(self):
        self.clear()
        self.write(f"Score: {self.score} | Highest Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def __add_score(self):
        self.score += 1
        self.clear()
        self.update_score_screen()

    def __loser(self):
        self.goto(0, 0)
        self.color("blue")
        self.write("GAME OVER", align=ALIGNMENT, font=("Comic Sans MS", 40, "bold"))

    def __reset_the_board(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score_screen()

    def add(self):
        self.__add_score()

    def update_score_screen(self):
        self.__update_the_score()

    def game_over(self):
        self.__loser()

    def reset(self):
        self.__reset_the_board()
