from turtle import Turtle


class States(Turtle):
    def __init__(self, coordinates, state):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(coordinates)
        self.state = state
        self.show_text()

    def show_text(self):
        self.write(arg=self.state, font=("Arial", 6, "normal"), move=False, align="left")
