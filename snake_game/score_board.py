from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")

with open("data.txt") as file:
    current_high_score = file.read()
    current_high_score = int(current_high_score)


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = current_high_score
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.show_score()

    def increase_score(self):
        self.score += 1
        self.show_score()

    def show_score(self):
        self.clear()
        message = f"Score: {self.score} High Score: {self.high_score}"
        self.write(font=FONT, align=ALIGNMENT, move=False, arg=message)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file2:
                file2.write(str(self.high_score))
        self.score = 0
        self.show_score()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(font=FONT, align=ALIGNMENT, move=False, arg="GAME OVER")
