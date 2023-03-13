from turtle import Turtle

DISTANCE = 20


class MyTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)

    def move(self):
        self.forward(DISTANCE)

    def reset_position(self):
        self.goto(0, -280)

