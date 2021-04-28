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
states_to_learn = list_of_states

while correct_guesses < 50:
    answer = screen.textinput(title=f"{correct_guesses}/50 State Name", prompt="Guess the state? to exit type 'Exit'")
    if answer.capitalize() in list_of_states:
        index = list_of_states.index(answer.capitalize())
        state = StateOnMap(list_of_x_cor[index], list_of_y_cor[index], list_of_states[index])
        correct_guesses += 1
        states_to_learn.remove(answer.capitalize())

    elif answer.capitalize() == "Exit":
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break
    else:
        print("Try again.")


screen.exitonclick()



"""
#This is the code to get the coordinate for the click
def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()"""
