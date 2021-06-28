from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}


def get_new_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = word_data.sample()
    french_word = current_card['French'].item()
    canvas.itemconfig(word_text, text=f"{french_word}", fill="black")
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"].item(), fill="white")
    canvas.itemconfig(card_background, image=card_back)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
card_background = canvas.create_image(400, 263, image=card_front)
card_back = PhotoImage(file="images/card_back.png")
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)





x_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=x_image, highlightthickness=0, command=get_new_word)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=get_new_word)
known_button.grid(row=1, column=1)

word_data = pandas.read_csv("data/french_words.csv")




get_new_word()

window.mainloop()

