from tkinter import *

""" first create screen """
window = Tk()
window.minsize(width=200, height=100)
window.title("Mile To Km Converter")
window.config(padx=30, pady=25)


def mile_kilometer():  # this is our converter function km >>>> mile
    user_input = entry.get()
    kilometer = round(int(user_input)*1.6)
    result.config(text=kilometer)


""" create cte texts of our program"""
km_label = Label(text="Km", font=("Times", "15", "bold italic"))
km_label.grid(column=2, row=1)

mile_label = Label(text="Miles", font=("Times", "15", "bold italic"))
mile_label.grid(column=2, row=0)

is_equal = Label(text="Is equal to", font=("Times", "15", "bold italic"))
is_equal.grid(column=0, row=1)

""" create a box for get the number from user """
entry = Entry(width=10)
entry.grid(column=1, row=0)

""" a number as a label,this is gonna change in each turn"""
result = Label(text=0, font=("Times", "15", "bold italic"))
result.grid(column=1, row=1)

""" the button of calculator 
    this button is relative to our converter function"""
button = Button(text="Calculate", command=mile_kilometer)
button.grid(column=1, row=2)


window.mainloop()
