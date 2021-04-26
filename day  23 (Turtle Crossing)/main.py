import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard


screen = Screen()
scoreboard = ScoreBoard()
screen.setup(width=600, height=600)
screen.bgcolor("spring green")
screen.title("Turtle Crossing")
screen.tracer(0)

turtle = Player()
cars = []

screen.listen()
screen.onkey(turtle.move, "Up")

game_over = False
while not game_over:
    time.sleep(0.1)
    screen.update()
    car = CarManager()
    cars.append(car)
    for car in cars:
        car.move(scoreboard.level)
        if turtle.ycor() > 280:
            scoreboard.add()
            turtle.goto(0, -280)
        if turtle.distance(car.car[0].xcor(), car.car[0].ycor()) < 20:
            scoreboard.game_over()
            game_over = True



screen.exitonclick()



