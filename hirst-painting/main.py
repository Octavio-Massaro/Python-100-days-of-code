from turtle import Turtle, Screen, colormode
import random


def change_direction(k):
    if k % 2 == 0:
        robin.setheading(180)
    else:
        robin.setheading(0)


colormode(255)
color_list = [(28, 107, 162), (190, 41, 82), (232, 161, 57), (232, 214, 90), (220, 138, 174), (140, 108, 59),
              (107, 193, 215), (22, 57, 130), (200, 165, 34), (210, 77, 94), (235, 89, 53), (119, 191, 144),
              (13, 151, 88), (143, 207, 225), (106, 108, 195), (136, 30, 70), (11, 183, 174), (97, 50, 37),
              (23, 157, 206), (229, 168, 186), (29, 92, 96), (84, 46, 33), (150, 214, 196), (175, 185, 222),
              (30, 47, 88), (232, 173, 165)]
robin = Turtle()
k = 0
direction = [0, 90, 180, 270]
robin.speed("fastest")

while k < 10:
    for i in range(9):
        robin.color(color_list[random.randint(0, 25)])
        robin.dot(20)
        robin.penup()
        robin.forward(50)
        robin.pendown()
        robin.dot(20)

    robin.penup()
    robin.setheading(90)
    robin.forward(50)
    change_direction(k)
    k += 1

screen = Screen()
screen.exitonclick()
