import time
from turtle import Screen

from ball import Ball
from moving_paddle import Paddle

screen = Screen()
screen.bgcolor("blue")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

paddle_1 = Paddle(375)
paddle_2 = Paddle(-375)
ball = Ball()

screen.listen()
screen.onkey(paddle_1.up, "Up")
screen.onkey(paddle_1.down, "Down")
screen.onkey(paddle_2.up, "w")
screen.onkey(paddle_2.down, "s")

game_over = False

while not game_over:
    screen.update()
    time.sleep(.1)
    ball.move()

screen.exitonclick()
