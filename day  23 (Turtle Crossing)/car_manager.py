import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "pink", "blue", "purple"]
STARTING_MOVE_DISTANCE = 2
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        self.car = []
        self.create()

    def __create_the_car(self):
        y_cor = random.randint(-280, 280)
        x_cor = random.randint(280, 500)
        color = random.choice(COLORS)
        for i in range(0, 2):
            i = Turtle(shape="square")
            i.penup()
            i.color(color)
            i.goto(x=x_cor, y=y_cor)
            i.setheading(180)
            self.car.append(i)
            x_cor -= 10
        return self.car

    def __move(self, speed):
        speed = STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * speed)
        y_cor = self.car[0].ycor()
        for item_num in range(len(self.car)):
            new_x = self.car[item_num].xcor() - speed
            self.car[item_num-1].goto(new_x, y_cor)
        self.car[item_num].forward(speed+20)

    def move(self, speed):
        self.__move(speed)

    def create(self):
        self.__create_the_car()



