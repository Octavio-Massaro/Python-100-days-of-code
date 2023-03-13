import turtle
import pandas as pd
from states import States


screen = turtle.Screen()
screen.title("Name The States")
screen.setup(width=720, height=505)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
is_game_on = True
states_list = data["state"].to_list()
users_state_list = []
state_length = len(states_list)

while is_game_on:
    users_state_length = len(users_state_list)
    if users_state_length == state_length:
        print("Congratulations, you've won the quiz")
        break
    answer_state = screen.textinput(title=f"Guess The State {users_state_length}/{state_length}", prompt="What's another state's name?")
    answer_state = answer_state.title()
    if answer_state in states_list and answer_state not in users_state_list:
        row = data[data["state"] == answer_state]
        x_cor = int(row["x"])
        y_cor = int(row["y"])
        states = States((x_cor, y_cor), answer_state)
        users_state_list.append(answer_state)

screen.exitonclick()
