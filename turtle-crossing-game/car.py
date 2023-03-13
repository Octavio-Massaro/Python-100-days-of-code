from turtle import Turtle, colormode
from random import randint

WEST = 180
colormode(255)
DISTANCE = 5


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.car_list = []
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.setheading(WEST)
        self.goto(280, randint(-250, 250))

    def move(self):
        for _ in self.car_list:
            _.forward(DISTANCE)

    def car_generator(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Car()
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            new_car.color(r, g, b)
            self.car_list.append(new_car)
