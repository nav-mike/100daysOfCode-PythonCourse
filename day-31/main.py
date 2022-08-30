from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv").to_dict(orient="records")

current_word = random.choice(data)

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=20, pady=20)


wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")


def flip_card():
    window.after_cancel(flip_card_timer)
    canvas.itemconfig(word_str_id, text=current_word['English'])
    canvas.itemconfig(lang_str_id, text="English")
    canvas.itemconfig(canvas_img_id, image=card_back_img)


flip_card_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)


def draw_word(word) -> int:
    return canvas.create_text(400, 263, text=word, font=("Helvetica", 100, "bold"), fill="black")


canvas_img_id = canvas.create_image(400, 263, image=card_front_img)
lang_str_id = canvas.create_text(400, 150, text="French", font=("Helvetica", 60, "italic"), fill="black")
word_str_id = draw_word(current_word['French'])
canvas.grid(row=0, column=0, columnspan=2)


def next_card():
    global current_word
    global word_str_id
    global flip_card_timer

    window.after_cancel(flip_card_timer)
    current_word = random.choice(data)
    canvas.delete(word_str_id)
    word_str_id = draw_word(current_word['French'])
    canvas.itemconfig(lang_str_id, text="French")
    canvas.itemconfig(canvas_img_id, image=card_front_img)
    flip_card_timer = window.after(3000, flip_card)


wrong_btn = Button(image=wrong_img, command=next_card, highlightthickness=0,
                   highlightbackground=BACKGROUND_COLOR)
right_btn = Button(image=right_img, command=next_card, highlightthickness=0,
                   highlightbackground=BACKGROUND_COLOR)

wrong_btn.grid(row=1, column=0)
right_btn.grid(row=1, column=1)

window.mainloop()
