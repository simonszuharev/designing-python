import turtle
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.create()

    def __create_the_turtle(self):
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def __move(self):
        self.forward(MOVE_DISTANCE)

    def create(self):
        self.__create_the_turtle()

    def move(self):
        self.__move()

    def start_over(self):
        turtle.goto(STARTING_POSITION)
