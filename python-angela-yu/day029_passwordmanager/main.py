from tkinter import *
from tkinter import messagebox
import random
import pyperclip

FONT = ("Calibri", 10, "normal")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ini hasil copas dari pw-generator-angela.py
# dan bakal dimodifikasi

#Password Generator Project
def generate_pw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    password = "".join(password_list)
    input_pw.insert(0, password)

    # buat copas otomatis pw yang udah di-generate ke clipboard
    # biar bisa langsung dipake passwordnya
    # jadi ga usah copy manual lagi
    pyperclip.copy(password)


    # gimana kalau double click generate password?
    # pengennya delete dulu baru generate pw baru lagi
    # tapi, pending dulu aja

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    data_website = input_website.get()
    data_username = input_username.get()
    data_pw = input_pw.get()
    data = f"{data_website} | {data_username} | {data_pw}\n"

    # # buat ngetes:
    # print(data_website)
    # print(data_username)
    # print(data_pw)
    # print(data)

    # kalau ada field / entry kosong, kasih popup buat ngingetin user
    if len(data_website) == 0 or len(data_username) == 0 or len(data_pw) == 0:
        messagebox.showinfo(title="Ups", message="Masih ada jawaban kosong, diisi dulu ya")
    else:
        # sebelum save, tanya user, udah yakin belum?
        # klik ok / cancel

        is_ok = messagebox.askokcancel(title=data_website, message=f"Ini data yang mau kamu masukin: \nEmail: {data_username}\nPassword: {data_pw}\nLanjut simpan?")

        if is_ok:
            with open("day029_passwordmanager/data.txt", mode='a') as file:
                file.write(data)
            
            input_website.delete(0, len(data_website))
            input_pw.delete(0, len(data_pw))

# ket:
# simpen semua input yang udah di add user pas klik add, ke file data.txt
# pakai open with buat save, pakai write
# terus kalau udah di add, delete semua entry yang udah diketik sebelumnya, pakai delete nya tkinter

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


# ======
# LAYOUT
# ======

# kita pakai grid layout (row, col)
# 0,0     0,1     0,2
# 1,0     1,1     1,2
# 2,0     2,1     2,2
# 3,0     3,1     3,2
# 4,0     4,1     4,2

# ==============================================
# BIKIN CANVAS ISINYA GAMBAR GEMBOK (GRID (0,1))
# ==============================================

canvas = Canvas(width=200, height=200)
gembok_img = PhotoImage(file="day029_passwordmanager/logo.png")
canvas.create_image(100, 100, image=gembok_img)
canvas.grid(row=0, column=1)

# ================================
# BIKIN LABEL WEBSITE (GRID (1,0))
# ================================

label_website = Label(text="Website:", font=FONT)
label_website.grid(row=1, column=0)

# =======================================
# BIKIN LABEL EMAIL/USERNAME (GRID (2,0))
# =======================================

label_emailusername = Label(text="Email/Username:", font=FONT)
label_emailusername.grid(row=2, column=0)

# =================================
# BIKIN LABEL PASSWORD (GRID (3,0))
# =================================

label_password = Label(text="Password:", font=FONT)
label_password.grid(row=3, column=0)

# =======================================
# BIKIN TOMBOL ADD (GRID (4,1)) COLSPAN 2
# =======================================

tombol_add = Button(text="Add", command=save, width=36, font=FONT)
tombol_add.grid(row=4, column=1, columnspan=2)

# ===========================================
# BIKIN TOMBOL GENERATE PASSWORD (GRID (3,2))
# ===========================================

tombol_generatepw = Button(text="Generate Password", command=generate_pw, font=FONT, width=15)
tombol_generatepw.grid(row=3, column=2)

# ==========================================
# BIKIN ENTRY WEBSITE (GRID (1,1)) COLSPAN 2
# ==========================================

input_website = Entry(width=35)
input_website.grid(row=1, column=1, columnspan=2)
input_website.focus() # biar bisa langsung ngetik usernya

# =================================================
# BIKIN ENTRY EMAIL/USERNAME (GRID (2,1)) COLSPAN 2
# =================================================

input_username = Entry(width=35)
input_username.grid(row=2, column=1, columnspan=2)
# biar ga usah ketik-ketik email lagi kalau pakai satu email yang itu-itu aja
input_username.insert(0, "dina@mail.com") # 0 itu merepresentasikan posisi cursor ketik (index). opsi lain, pakai END buat narok cursor ketik di akhir text

# =================================
# BIKIN ENTRY PASSWORD (GRID (3,1))
# =================================

input_pw = Entry(width=21)
input_pw.grid(row=3, column=1)


window.mainloop()
