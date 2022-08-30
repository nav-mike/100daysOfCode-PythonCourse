from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_SEC = 25
SHORT_BREAK_SEC = 5
LONG_BREAK_SEC = 20

# ---------------------------- TIMER RESET ------------------------------- # 


def reset() -> None:
    global reps
    global mark_sign

    reps = 0
    mark_sign = ""
    window.after_cancel(timer)
    label.config(text="Timer", fg=GREEN)
    start_btn.config(state=NORMAL)
    reset_btn.config(state=DISABLED)

# ---------------------------- TIMER MECHANISM ------------------------------- #


reps = 0
mark_sign = ""
timer = ""

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def show_time(value: int) -> str:
    return f"{math.floor(value / 60)}:{value % 60:02d}"


def count_down(count: int) -> None:
    global timer

    if count > 0:
        canvas.itemconfig(timer_text, text=show_time(count))
        timer = window.after(1000, count_down, count - 1)
    else:
        canvas.itemconfig(timer_text, text="00:00")
        start_btn.config(state=NORMAL)
        mark_label.config(text=mark_sign)


def start_timer():
    global reps
    global mark_sign

    start_btn.config(state=DISABLED)
    reset_btn.config(state=NORMAL)

    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_SEC)
        label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_SEC)
        label.config(text="Break", fg=PINK)
    else:
        mark_sign = f"✓{mark_sign}"
        count_down(WORK_SEC)
        label.config(text="Work", fg=GREEN)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text=show_time(0), font=(FONT_NAME, 35, "bold"), fill="white")

label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))

start_btn = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
reset_btn = Button(text="Reset", highlightbackground=YELLOW, state=DISABLED, command=reset)

mark_label = Label(text=mark_sign, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))

label.grid(column=1, row=0)
canvas.grid(column=1, row=1)
start_btn.grid(column=0, row=2)
reset_btn.grid(column=2, row=2)
mark_label.grid(column=1, row=3)

window.mainloop()
