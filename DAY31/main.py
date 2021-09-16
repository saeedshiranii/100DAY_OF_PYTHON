from pandas import read_csv
from random import choice
from tkinter import *
import pandas

current_card = {}
data_as_dict = {}


try:
    data = read_csv("data/words.csv")

except FileNotFoundError:
    data = read_csv("data/french_words.csv")
    data_as_dict = data.to_dict(orient="records")

else:
    data_as_dict = data.to_dict(orient="records")


def to_learn():
    data_as_dict.remove(current_card)
    words_to_learn = pandas.DataFrame(data_as_dict)
    words_to_learn.to_csv("data/words.csv")
    next_card()


def next_card():
    global current_card, turn_timer
    window.after_cancel(turn_timer)
    current_card = choice(data_as_dict)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_img, image=card_front_img)
    turn_timer = window.after(3000, func=turn_card)


def turn_card():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_img, image=card_back_img)


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
turn_timer = window.after(3000, func=turn_card)


canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

card_img = canvas.create_image(400, 263, image=card_front_img)
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=to_learn)
known_button.grid(row=1, column=1)


next_card()

window.mainloop()
