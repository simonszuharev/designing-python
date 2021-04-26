import turtle
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.create()

    def __create_the_turtle(self):
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def __move(self):
        self.forward(MOVE_DISTANCE)

    def __go_to_start_now(self):
        self.goto(STARTING_POSITION)

    def go_to_start(self):
        self.__go_to_start_now()

    def create(self):
        self.__create_the_turtle()

    def move(self):
        self.__move()

    def finished(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
