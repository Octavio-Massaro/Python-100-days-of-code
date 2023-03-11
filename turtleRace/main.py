from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which Turtle will win the race? Enter a color: (The colors "
                                                          "are: purple,blue,green,yellow,orange and red)")
user_bet = user_bet.lower()
colors = ["purple", "blue", "green", "yellow", "orange", "red"]
turtles = []
i = 0
cord_y = -100
for turtle_color in colors:
    turtles.append(Turtle(shape="turtle"))
    turtles[i].color(turtle_color)
    turtles[i].penup()
    turtles[i].goto(x=-239, y=cord_y)
    i += 1
    cord_y += 40

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_turtle = turtle.pencolor()
            is_race_on = False
            if winning_turtle == user_bet:
                print(f"You've won! The winning turtle was: {winning_turtle}")
                break
            else:
                print(f"You've lose! The winning turtle was: {winning_turtle}")
                break
        turtle.forward(random.randint(0, 10))

screen.exitonclick()
