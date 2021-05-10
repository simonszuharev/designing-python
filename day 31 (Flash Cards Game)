import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
words_to_learn = {}
current_card = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    words_to_learn = original_data.to_dict(orient="records")
else:
    words_to_learn = data.to_dict(orient="records")


def show_word():
    global current_card, timer
    window.after_cancel(timer)
    canvas.itemconfig(card_bg, image=front_card)
    current_card = random.choice(words_to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card['French'], fill="black")
    timer = window.after(3000, func=flipped_card)


def known_word():
    words_to_learn.remove(current_card)
    data = pandas.DataFrame(words_to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    show_word()

def flipped_card():
    canvas.itemconfig(card_bg, image=back_card)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card['English'], fill="white")


# Window
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, func=flipped_card)

# Card Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=front_card)
card_title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Right Button

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=known_word)
right_button.grid(column=1, row=1)

# Wrong Button

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=show_word)
wrong_button.grid(column=0, row=1)

show_word()  # to avoid blank card when running the program

window.mainloop()
