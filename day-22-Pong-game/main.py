import time
from turtle import Screen

from ball import Ball
from moving_paddle import Paddle
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("blue")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

paddle_1 = Paddle(375)
paddle_2 = Paddle(-375)
ball = Ball()
scoreboard_1 = ScoreBoard(-100, 200)
scoreboard_2 = ScoreBoard(100, 200)

screen.listen()
screen.onkey(paddle_1.up, "Up")
screen.onkey(paddle_1.down, "Down")
screen.onkey(paddle_2.up, "e")
screen.onkey(paddle_2.down, "s")

game_over = False

while not game_over:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    paddle_1.ball_touch(ball)
    paddle_2.ball_touch(ball)
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard_1.add()
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard_2.add()


screen.exitonclick()



