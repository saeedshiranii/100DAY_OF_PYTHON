from tkinter import *
from random import choice
from pandas import read_csv

data = read_csv("data/french_words.csv")
data_as_dict = data.to_dict(orient="records")


def fr_card():
    choose_dict = choice(data_as_dict)
    canvas.itemconfig(title, text="French")
    canvas.itemconfig(word, text=choose_dict["French"])



BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)


next_card()

window.mainloop()
