import time
from turtle import Screen, Turtle
from food import Food
from scoreboard import ScoreBoard
from snake import Snake

"""
def if_border(list):
    for item in list:
        if item.position() == """

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("spring green")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_over = False


while not game_over:
    screen.update()
    time.sleep(.1)
    snake.move()

    #Food Collision
    if snake.head.distance(food) < 15:
        food.refresh_location()
        snake.add_element()
        scoreboard.add()


    #GameOver
    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.xcor() > 290:
        scoreboard.reset()
        snake.reset()
        #scoreboard.game_over()

    #Detect collision
    for element in snake.list_snake[1:]:
        if snake.head.distance(element) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
