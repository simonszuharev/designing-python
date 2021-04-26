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

player = Player()
cars = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

game_over = False

while not game_over:
    time.sleep(0.1)
    screen.update()

    cars.create()
    cars.move()

    # detect collision
    for car in cars.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_over = True

    # detect if finished
    if player.finished():
        player.go_to_start()
        cars.level_up()
        scoreboard.add()

screen.exitonclick()
