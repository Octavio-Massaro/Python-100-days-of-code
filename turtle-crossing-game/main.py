from turtle import Screen
from my_turtle import MyTurtle
from score import Score
from car import Car
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing The Street Game")
screen.tracer(0)

robin = MyTurtle()
score = Score()
car = Car()

screen.listen()
screen.onkeypress(fun=robin.move, key="w")
is_game_on = True


while is_game_on:
    time.sleep(score.car_speed)
    screen.update()
    car.car_generator()
    car.move()
    if robin.ycor() > 270:
        score.increase_score()
        robin.reset_position()

    for _ in car.car_list:
        if robin.distance(_) < 20:
            is_game_on = False
            score.end_game()
            break

screen.exitonclick()
