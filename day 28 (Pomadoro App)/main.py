from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="TIMER")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break)
        title.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break)
        title.config(text="BREAK", fg=PINK)
    else:
        countdown(work_sec)
        title.config(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checks = ""
            work_sessions = math.floor(reps / 2)
            for mark in range(work_sessions):
                checks += "✔"
            check_marks.config(text=checks)


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Pomadoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Title

title = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
title.grid(column=1, row=0)

# Tomato Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_background = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_background)
timer_text = canvas.create_text(100, 130, text="00:00", fill=YELLOW, font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Start button
start_button = Button(text="start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=3)

# Reset button
reset_button = Button(text="reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=3)

# Check mark

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
