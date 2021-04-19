from turtle import Turtle, Screen
import random


def assign_colors(list_of_turtles):
    for i in list_of_turtles:
        color = random.choice(colors)
        i.color(color)
        colors.remove(color)
    return list_of_turtles


def assign_position(list_of_turtles):
    y = -120
    for i in list_of_turtles:
        i.penup()
        i.goto(x=-240, y=y)
        y += 40


screen = Screen()

colors = ['red', 'orange', 'gold', 'green', 'blue', 'deep sky blue', 'purple']
screen.setup(width=500, height=400)
finish = False
user_bet = screen.textinput(title="Bet Decision",
                            prompt="Who's gonna win the race? Choose between 'red', 'orange', 'gold', 'green', 'blue', 'deep sky blue', 'purple'")

# creating turtles that will race

turtles = []

for new_turtle in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.shapesize(2, 2, 4)
    turtles.append(new_turtle)

assign_colors(turtles)
assign_position(turtles)

if user_bet:
    finish = False

while not finish:
    for turtle in turtles:
        if turtle.xcor() > 230:
            finish = True
            if user_bet == turtle.pencolor():
                print(f"Congrats! The {turtle.pencolor()} turtle won! You're lucky :) ")
            else:
                print(f"The winner is {turtle.pencolor()}! Not your best shot, dude :( Try again.")

        jump_distance = random.randint(0, 15)
        turtle.forward(jump_distance)

screen.exitonclick()
