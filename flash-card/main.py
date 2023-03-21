import pandas
from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}

try:
    df = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("./data/french_words.csv")
    to_learn = df.to_dict(orient="records")
else:
    to_learn = df.to_dict(orient="records")


def change_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(flash_card, image=card_front_image)
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(title_card, text="French", fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(title_card, text="English", fill="white")
    canvas.itemconfig(flash_card, image=card_back_image)


def is_known():
    to_learn.remove(current_card)
    dfr = pandas.DataFrame(to_learn)
    dfr.to_csv("data/words_to_learn.csv", index=False)
    change_word()


window = Tk()
window.title("Flash Card")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card = canvas.create_image(400, 263, image=card_front_image)
title_card = canvas.create_text(400, 150, text="", font=("ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=change_word)
wrong_button.grid(row=1, column=0)

change_word()
window.mainloop()
