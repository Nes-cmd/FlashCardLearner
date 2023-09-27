import random
import time
from tkinter import *
import pandas
BACKGROUND_COLOR = "#B1DDC6"


try:
    my_data = pandas.read_csv("data/words_to_learn.csv")
except:
    print("first time")
    my_data = pandas.read_csv("data/french_words.csv")
finally:
    new_data = my_data.to_dict('records')
    print(new_data)

current_word = {}


def next_card():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(new_data)
    print(len(new_data))
    canvas.itemconfig(ctitle, text="English", fill="black")
    canvas.itemconfig(cword, text=current_word["English"], fill="black")
    canvas.itemconfig(cimage, image=card_front_image)
    flip_timer = window.after(3000, flip_card)
def flip_card():
    canvas.itemconfig(ctitle, text="French", fill="white")
    canvas.itemconfig(cword, text=current_word["French"], fill="white")
    canvas.itemconfig(cimage, image=card_back_image)
def known_word():
    new_data.remove(current_word)
    to_learn = pandas.DataFrame(new_data)
    to_learn.to_csv("data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flashy")
flip_timer = window.after(3000, flip_card)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526)

card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
cimage = canvas.create_image(400, 263, image=card_front_image)
ctitle = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
cword = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Cross button
cross_image = PhotoImage(file="images/wrong.png")
un_button = Button(image=cross_image)
un_button.config(border=0, bg=BACKGROUND_COLOR, borderwidth=0, highlightthickness=0, command=next_card)
un_button.grid(row=1, column=0)

# Right button
check_image = PhotoImage(file="images/right.png")
kn_button = Button(image=check_image)
kn_button.config(highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0, command=known_word)
kn_button.grid(row=1, column=1)

next_card()

window.mainloop()

