import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
turn = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(canvas_text, text='00:00')
    timer_label.config(text="Timer")
    tik_label.config(text="")
    global turn
    turn = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def starter():
    global turn
    turn += 1
    if turn in (1, 3, 5, 7):

        work_sec = WORK_MIN * 60
        timer_label.config(text="Work", font=(FONT_NAME, 40, "bold"), fg=GREEN, highlightthickness=0, bg=YELLOW)
        timer_label.grid(row=0, column=1)
        counter(work_sec)

    elif turn in (2, 4, 6):
        tiny_break_sec = SHORT_BREAK_MIN * 60
        timer_label.config(text="Break", font=(FONT_NAME, 40, "bold"), fg=PINK, highlightthickness=0, bg=YELLOW)
        timer_label.grid(row=0, column=1)
        counter(tiny_break_sec)

    elif turn == 8:
        long_break_sec = LONG_BREAK_MIN * 60
        timer_label.config(text="Rest", font=(FONT_NAME, 40, "bold"), fg=RED, highlightthickness=0, bg=YELLOW)
        timer_label.grid(row=0, column=1)
        counter(long_break_sec)
        #turn = 0
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def counter(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = F"0{count_sec}"
    global timer
    canvas.itemconfig(canvas_text, text=F"{count_min}:{count_sec}")

    if count > 0:
        timer = window.after(1000, counter, count-1)

    else:
        starter()
        mark = ""
        done_tik = math.floor(turn/2)
        for _ in range(done_tik):
            mark += "✔"
        tik_label.config(text=mark)



# ---------------------------- UI SETUP ------------------------------- #
# Todo: create a window
window = Tk()
window.title("Tomato timer")
window.config(padx=100, pady=50, bg="#f7f5dd")


""" create canvas and image """
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tom_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 110, image=tom_img)
canvas_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 28, "bold"))
canvas.grid(row=1, column=1)


""" create labels """
timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, highlightthickness=0, bg=YELLOW)
timer_label.grid(row=0, column=1)

tik_label = Label(fg=GREEN, font=(FONT_NAME, 10, "bold"), highlightthickness=0, bg=YELLOW )
tik_label.grid(row=3, column=1)

""" create buttons """
reset_button = Button(text='Reset', highlightthickness=0, bg="#9bdeac", command=reset)
reset_button.grid(row=2, column=2)

start = Button(text='Start ', highlightthickness=0, bg="#9bdeac", command=starter)
start.grid(row=2, column=0)

window.mainloop()
