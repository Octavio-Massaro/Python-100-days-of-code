from turtle import Turtle

DISTANCE = 20
NORTH = 90


class Paddle(Turtle):
    def __init__(self, coordinate):
        super().__init__()
        self.coordinate = coordinate
        self.shape("square")
        self.color("white")
        self.setheading(NORTH)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.speed("fastest")
        self.goto(self.coordinate)

    def up(self):
        if self.ycor() < 250:
            self.forward(DISTANCE)

    def down(self):
        if self.ycor() > -240:
            self.backward(DISTANCE)
