from tkinter import *
""" This is my first GUI project """
win = Tk()
win.title('my first GUI *__* ')
win.geometry("800x500")


def change_label():
    u_entry = entry.get()
    label.config(text=u_entry)


label = Label(text="It's Started ", font=("Times", "24", "bold italic"))
label.pack()

entry = Entry(width=30)
entry.pack()

button = Button(text="tap on me :)) ", font=("Times", "10", "bold"), command=change_label)
button.pack()


win.mainloop()
