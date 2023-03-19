from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def clear():
    website_entry.delete(0, END)
    email_username_entry.delete(0, END)
    password_entry.delete(0, END)


def warn(entry):
    messagebox.showwarning(title="Empty field", message="Please fill the field " + entry)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    if len(password_entry.get()) > 0:
        password_entry.delete(0, END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    if len(website) == 0:
        warn("website")
    elif len(email) == 0:
        warn("email")
    elif len(password) == 0:
        warn("password")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"You would like to Save this email and password:\n Email: {email},\n Password: {password}")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website}  |  {email}  |  {password}\n")
            clear()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=40)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)

email_username_entry = Entry(width=40)
email_username_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", command=password_generator)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
