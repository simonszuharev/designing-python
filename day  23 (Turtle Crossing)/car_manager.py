import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "pink", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def __create_the_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            color = random.choice(COLORS)
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(color)
            y_cor = random.randint(-250, 250)
            new_car.goto(300, y_cor)
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def __move(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def __level_up(self):
        self.car_speed += MOVE_INCREMENT

    def level_up(self):
        self.__level_up()

    def move(self):
        self.__move()

    def create(self):
        self.__create_the_car()





