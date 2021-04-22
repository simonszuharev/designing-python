from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def __move_the_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def __bounce(self):
        self.y_move *= -1

    def __bounce_back(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def __reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.x_move *= -1
        self.move()

    def bounce_back(self):
        self.__bounce_back()

    def bounce(self):
        self.__bounce()

    def move(self):
        self.__move_the_ball()

    def reset_position(self):
        self.__reset_position()
