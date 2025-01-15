BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"

from tkinter import *
import pandas as pd
import random



# ---------------------------- READ CSV ------------------------------- #

kamus_france = pd.read_csv("day031_flashcard/data/french_words.csv")

# ---------------------------- FUNGSI GANTI CARD ------------------------------- #

def ganti_card():

    canvas.itemconfig(word_text, text=f"{random.choice(kamus_france["French"])}")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("French Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# ======
# LAYOUT
# ======

# kita pakai grid layout (row, col)
# 0,0     0,1
# 1,0     1,1




# ========================================================
# BIKIN CANVAS ISINYA GAMBAR GEMBOK (GRID (0,0)) COLSPAN 2
# ========================================================

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_img = PhotoImage(file="day031_flashcard/images/card_back.png")
card_front_img = PhotoImage(file="day031_flashcard/images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="French", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=(FONT_NAME, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


# ================================
# BIKIN TOMBOL SILANG (GRID (1,0))
# ================================

silang_img = PhotoImage(file="day031_flashcard/images/wrong.png")
tombol_silang = Button(image=silang_img, command=ganti_card, highlightthickness=0, bg=BACKGROUND_COLOR)
tombol_silang.grid(row=1, column=0)


# ================================
# BIKIN TOMBOL CEKLIS (GRID (1,1))
# ================================

ceklis_img = PhotoImage(file="day031_flashcard/images/right.png")
tombol_ceklis = Button(image=ceklis_img, command=ganti_card, bg=BACKGROUND_COLOR, highlightthickness=0)
tombol_ceklis.grid(row=1, column=1)

window.mainloop()