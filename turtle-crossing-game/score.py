from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-175, 250)
        self.score = 0
        self.show_score()
        self.car_speed = 0.1

    def show_score(self):
        self.clear()
        self.write(f"Level: {self.score}", align=ALIGNMENT, font=FONT, move=False)

    def increase_score(self):
        self.score += 1
        self.show_score()
        self.car_speed *= 0.9

    def end_game(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT, move=False)
