import turtle
import pandas
from state_turtle import StateOnMap

screen = turtle.Screen()

screen.title("US States Game 🇺🇸")
image = "blank_states_img.gif"  # map
screen.addshape(image)  # adding the map as the background
turtle.shape(image)
correct_guesses = 0

data = pandas.read_csv("50_states.csv")
list_of_states = data["state"].to_list()
list_of_x_cor = data["x"].to_list()
list_of_y_cor = data["y"].to_list()

while correct_guesses < 50:
    answer = screen.textinput(title=f"{correct_guesses}/50 State Name", prompt="Guess the state?")
    if answer.capitalize() in list_of_states:
        index = list_of_states.index(answer.capitalize())
        state = StateOnMap(list_of_x_cor[index], list_of_y_cor[index], list_of_states[index])
        correct_guesses += 1
    else:
        print("Try again.")
        

screen.exitonclick()



"""
#This is the code to get the coordinate for the click
def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()"""
