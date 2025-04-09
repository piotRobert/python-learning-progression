from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FILE_PATH = "d31_flash_cards/images"
LANGUAGE = "French"
TRANSLATION = "English"
current_card = {}
to_learn = {}

try:
    data = df = pandas.read_csv("d31_flash_cards/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("d31_flash_cards/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def flip_card():
    canvas.itemconfig(flash_card_image, image=card_back_image)
    canvas.itemconfig(language_text, text=TRANSLATION, fill="white")
    canvas.itemconfig(word_text, text=current_card[TRANSLATION], fill="white")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    
    canvas.itemconfig(language_text, text=LANGUAGE, fill="black")
    canvas.itemconfig(word_text, text=current_card[LANGUAGE], fill="black")
    canvas.itemconfig(flash_card_image, image=card_front_image)

    flip_timer = window.after(3000, func=flip_card)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("d31_flash_cards/data/words_to_learn.csv", index=False)
    next_card()

#  UI
window = Tk()
window.title("Flashy")
window.config(padx = 50, pady = 50, background=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file=f"{FILE_PATH}/card_front.png")
card_back_image = PhotoImage(file=f"{FILE_PATH}/card_back.png")
flash_card_image = canvas.create_image(400, 263, image=card_front_image)
language_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0,column=0, columnspan=2)

wrong_image = PhotoImage(file=f"{FILE_PATH}/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1,column=0)

right_image = PhotoImage(file=f"{FILE_PATH}/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1,column=1)

next_card()

window.mainloop()