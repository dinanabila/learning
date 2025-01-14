from tkinter import *
# kita import nya kek di atas, 
# soalnya modul yang dipakai cuma 1
# jadi gpp, ga ada potensi kecampur sama modul lain soalnya


window = Tk()
window.title("GUI pertama acuu")
window.minsize(width=500, height=300)

# kasih jarak padding biar enak diliat, kek margin lah ibaratnya
window.config(padx=100, pady=200)
# padx sama pady juga bisa dipakai di widget buat ngasih margin, 
# jadi ga cuma bisa buat windows aja


# bikin label

my_label = Label(text="hai aku label", font=("Arial", 20))
# buat benerin nampilin label nya di window:
my_label.grid(column=0, row=0)

# opsi lain:
# my_label.pack()


# buat ganti teks bisa kek gini, ada 2 cara yang bisa dipilih:
my_label["text"] = "New Text"
my_label.config(text="New Text")


# Button

def button_clicked():
    print("I got clicked")
    teks_baru = input.get()
    my_label.config(text=teks_baru)


button = Button(text="Klik acuu", command=button_clicked)

# janlup ini biar button nya kepajang di gui nya
button.grid(column=1, row=1)

# button.pack()

new_button = Button(text="klik acu ajaaa", command=button_clicked)
new_button.grid(column=2, row=0)


# Entry

input = Entry(width=10)
# input.pack()
# input2 = Entry(width=10)

input.grid(column=3, row=2)
# input2.pack()




window.mainloop()