BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
comot_kata = {}

from tkinter import *
import pandas as pd
import random



# ---------------------------- READ CSV ------------------------------- #

data = pd.read_csv("day031_flashcard/data/french_words.csv")

# tambahan dari angela:

kamus_france = data.to_dict(orient="records") 
# orient records ini biar dict keluarannya bisa jadi bentuk kamus--
# france-english beneran per masing-masing katanya
# jadi berguna banget biar kerjaannya ga sulit dan bertele-tele

# bentuknya itu jadinya list, yang isinya dict dict
# tiap dict isinya 1 kata france-english

# ini contoh sampelnya:
# print(kamus_france)
# [{'French': 'partie', 'English': 'part'}, {'French': 'histoire', 'English': 'history'},


# ---------------------------- FUNGSI HAPUS KATA ------------------------------- #

# fungsi ini dipakai sama tombol ceklis
# wordnya bakal kehapus dari kamus pas user klik ceklis
# soalnya udah dikuasai, ga usah dipelajari lagi

def hapus_kata():
    global comot_kata
    try:
        kamus_france.remove(comot_kata)
    except ValueError:
        canvas.itemconfig(card_title, text="Selamat!", fill="white", font=(FONT_NAME, 40, "bold"))
        canvas.itemconfig(card_word, text="Kamu berhasil! 'v')b", fill="white", font=(FONT_NAME, 30, "bold"))
    else:
        # # =============================
        # # buat debug
        print(f"{comot_kata} terhapus")
        # print(kamus_france)
        # # =============================

        words_to_learn = pd.DataFrame(kamus_france)
        words_to_learn.to_csv("day031_flashcard/data/words_to_learn.csv", index=False)

        ganti_card()


# ---------------------------- FUNGSI GANTI CARD ------------------------------- #

def ganti_card():
    global comot_kata, timer_balik_kartu
    # ===================
    # ini buat handle bug 
    window.after_cancel(timer_balik_kartu)
    # ===================
    try:
        comot_kata = random.choice(kamus_france)
    except IndexError:
        canvas.itemconfig(card_title, text="Selamat!", fill="white", font=(FONT_NAME, 40, "bold"))
        canvas.itemconfig(card_word, text="Kamu berhasil 'v')b", fill="white", font=(FONT_NAME, 30, "bold"))
    else:
        french_text = comot_kata["French"]
        canvas.itemconfig(card_title, text="French", fill="black")
        canvas.itemconfig(card_word, text=french_text, fill="black")
        canvas.itemconfig(card_background, image=card_front_img)

        # buat itung mundur 3 detik, abis itu balik kartu
        timer_balik_kartu = window.after(3000, balik_card)

    # UNTUK BUG KLIK SEBELUM BALIK KARTU
    # SOLUSINYA BIKIN GLOBAL CONSTANT BARU
    # TERUS JUGA TIMER NYA MASUKIN VARIABEL
    # BIAR SI VARIABEL ITU BISA KITA MASUKIN KE AFTER_CANCEL() NYA TKINTER

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def balik_card():
    global comot_kata
    english_text = comot_kata["English"]
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=english_text, fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("French Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# ini juga harus ditarok di sini, 
# supaya kedeteksi pas mau cancel timernya di fungsi ganti_card()
timer_balik_kartu = window.after(3000, balik_card)

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
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))
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
tombol_ceklis = Button(image=ceklis_img, command=hapus_kata, bg=BACKGROUND_COLOR, highlightthickness=0)
tombol_ceklis.grid(row=1, column=1)


ganti_card()

window.mainloop()