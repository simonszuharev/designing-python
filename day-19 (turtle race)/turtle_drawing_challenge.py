from turtle import Turtle, Screen

screen = Screen()
my_turtle = Turtle()


def clear():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()


def move_forward():
    my_turtle.forward(10)


def move_backward():
    my_turtle.backward(10)


def turn_right():
    new_direction = my_turtle.heading() - 10
    my_turtle.setheading(new_direction)


def turn_left():
    new_direction = my_turtle.heading() + 10
    my_turtle.setheading(new_direction)


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
