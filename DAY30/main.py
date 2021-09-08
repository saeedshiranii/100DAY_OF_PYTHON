from tkinter import messagebox
from random import choice
from tkinter import *
import pyperclip
import json

""" this program is same with yesterday project but i used json for manage the data """


""" a list for generate password"""
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
MASTER_LIST =['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '/',
              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>',
              '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
              'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', ']',
              '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
              'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{',
              '|', '}', '~']


def random_pass_generator():
    password = ""
    for _ in range(0, 10):
        ran_pas_gen = choice(MASTER_LIST)
        password += ran_pas_gen

    password_entry.insert(0, password)
    pyperclip.copy(password)


#SAVE PASSWORD
def save():
    get_password = password_entry.get()
    get_email = email_entry.get()
    get_website = website_entry.get()
    data_as_dict = {
        get_website: {
            "email": get_email,
            "password": get_password
        }
    }

    if len(get_website) == 0 or len(get_email) == 0 or len(get_password) == 0:
        messagebox.showinfo(title="Error", message="Please make sure you have not left any box empty.")

    else:
        is_ok = messagebox.askokcancel(title=get_website, message=F"These are the details entered: \n "
                                                                  F"Email: {get_email} \n "
                                                                  F"Password: {get_password} is it ok to save ?")
        try:
            with open("password.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("password.json", "w") as file:
                json.dump(data_as_dict, file, indent=4)

        else:
            data.update(data_as_dict)
            with open("password.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            messagebox.showinfo(title="Password manager", message="Your data is saved.")
            password_entry.delete(0, END)
            website_entry.delete(0, END)


# def search():
#     web_order =website_entry.get()
#     with open("password.json", "r") as a_file:
#         file = a_file.read()
#         # for site in file:
#         #     if site == web_order:
#         #         print(web_order["password"])
#         print(file)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password manager")
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

""" create canvas and image """
canvas = Canvas(width=200, height=200)
img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

""" Create labels """
website_label = Label(text="Website")
email_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

""" Sort our labels """
website_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

""" Create boxes """
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1)
email_entry.insert(0, "saeed_is_awesome@gmail.com")
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)

""" Create buttons """
password_button = Button(text="Generate Password", command=random_pass_generator)
password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=5, column=1)
#search_button = Button(text="           Search        ", command=search)
#search_button.grid(row=1, column=2)


window.mainloop()
