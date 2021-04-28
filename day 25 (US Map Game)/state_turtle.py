from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Comic Sans MS", 10, "normal")


class StateOnMap(Turtle):

    def __init__(self, x_cor, y_cor, state):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(x_cor, y_cor)
        self.write(state, align=ALIGNMENT, font=FONT)
