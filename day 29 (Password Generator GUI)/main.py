import time
from tkinter import *
from tkinter import messagebox
import random
import csv
import pyperclip

FONT_NAME = "Times New Roman"
FIELD_NAMES = ['website', 'email/username', 'password']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    password_entry.delete(0, END)
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = ''.join(password_list)
    pyperclip.copy(password)
    password_entry.insert(0, password)
    messagebox.showinfo(message="The password has been copied to your clipboard")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    data = {"website": website_entry.get(), "email/username": email_entry.get(), "password": password_entry.get()}
    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title="Error", message="Please, make sure to fill out all fields.")
    else:
        is_okay = messagebox.askokcancel(title=website_entry.get(),
                                         message=f"The details entered are: \n Website: {website_entry.get()} \n Email/Username"
                                                 f"{email_entry.get()} \n Password: {password_entry.get()} \n Is it okay to save?")

        if is_okay:
            with open('passwords.csv', 'a+', newline='') as csvfile:
                csvwriter = csv.DictWriter(csvfile, fieldnames=FIELD_NAMES)
                csvwriter.writerow(data)
                csvfile.close()
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20, bg="white")

# Lock Canvas
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_background = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_background)
canvas.grid(column=1, row=0)

# Website

website_label = Label(text="Website:", fg="black", bg="white", font=(FONT_NAME, 15, "bold"))
website_label.grid(column=0, row=1)
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

# Email/Username

email_label = Label(text="Email/Username:", fg="black", bg="white", font=(FONT_NAME, 15, "bold"))
email_label.grid(column=0, row=2)
email_entry = Entry(width=35)
email_entry.insert(0, "example@example.com")
email_entry.grid(column=1, row=2, columnspan=2)

# Password

password_label = Label(text="Password:", fg="black", bg="white", font=(FONT_NAME, 15, "bold"))
password_label.grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Button add

add_button = Button(text="Add", width=36, command=add)
add_button.grid(column=1, row=4, columnspan=2)

# Button Generate

checkbutton = Button(text="Generate Password", command=generate_password)
checkbutton.grid(column=2, row=3)

window.mainloop()
