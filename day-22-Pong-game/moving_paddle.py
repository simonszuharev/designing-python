import turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
TOP_BORDER = 280
BOTTOM_BORDER = -275


class Paddle:

    def __init__(self, x_position):
        self.paddle = []
        self.x_cor = x_position
        self.create()
        self.top = self.paddle[0]
        self.bottom = self.paddle[len(self.paddle)-1]

    def __create_the_paddle(self, x_cor):
        y = 40
        for i in range(0, 5):
            i = turtle.Turtle(shape="square")
            i.color("white")
            i.penup()
            i.goto(x=x_cor, y=y)
            y -= 20
            self.paddle.append(i)
        return self.paddle

    def __up_move(self, x_cor):
        if self.top.ycor() < TOP_BORDER:
            self.top.setheading(UP)
            for item_num in range(len(self.paddle) - 1, 0, -1):
                new_y = self.paddle[item_num - 1].ycor()
                self.paddle[item_num].goto(x_cor, new_y)
            self.top.forward(MOVE_DISTANCE)

    def __down_move(self, x_cor):
        if self.bottom.ycor() > BOTTOM_BORDER:
            self.top.setheading(DOWN)
            for item_num in range(len(self.paddle) - 1, 0, -1):
                new_y = self.paddle[item_num].ycor() - MOVE_DISTANCE
                self.paddle[item_num].goto(x_cor, new_y)
            self.top.forward(MOVE_DISTANCE)

    def create(self):
        self.__create_the_paddle(self.x_cor)

    def up(self):
        self.__up_move(self.x_cor)

    def down(self):
        self.__down_move(self.x_cor)
