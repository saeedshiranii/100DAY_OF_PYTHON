import time
from tkinter import *
from random import choice
import pandas

data = pandas.read_csv("data/french_words.csv")
data_dict = data.to_dict(orient="records")
print(data_dict)
chosen_dict = {}


def en_card():
    global chosen_dict
    word = chosen_dict["English"]
    language = "English"
    canvas.itemconfig(show_word, text=word, fill="white")
    canvas.itemconfig(show_title, text=language, fill="white")
    canvas.itemconfig(wallpaper, image=card_back_img)


def card():
    global chosen_dict
    chosen_dict = choice(data_dict)
    word = chosen_dict["French"]
    language = "French"
    canvas.itemconfig(wallpaper, image=card_front_img)
    canvas.itemconfig(show_word, text=word, fill="black")
    canvas.itemconfig(show_title, text=language, fill="black")

BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flash card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
start = time.time()
window.after(3, func=card)


canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

wallpaper = canvas.create_image(400, 263, image=card_front_img)
show_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
show_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=card)
known_button.grid(row=1, column=1)

stop = time.time()
total_time = stop - start
print(total_time)


if known_button and total_time <= 3:
    card()


elif total_time > 3:
    en_card()
    print('6')

window.mainloop()
