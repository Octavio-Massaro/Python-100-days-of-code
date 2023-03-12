from turtle import Turtle

FONT = ("arial", 24, "normal")
ALIGNMENT = "center"


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.position = position
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.score = 0
        self.generate_text()

    def generate_text(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, move=False, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.generate_text()
