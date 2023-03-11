from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.increase_score()

    def increase_score(self):
        self.clear()
        message = f"Score: {self.score}"
        self.write(font=FONT, align=ALIGNMENT, move=False, arg=message)
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(font=FONT, align=ALIGNMENT, move=False, arg="GAME OVER")
