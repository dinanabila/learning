import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for i in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

ketebak = [] # ini harus tarok di luar loop, supaya ga jadi kosong lagi pas loop nya balik ke awal

# TODO 1: Bikin while loop supaya user bisa nebak huruf lagi. 
while "_" in placeholder:
    guess = input("Tebak huruf (ketik + enter): ").lower()

# TODO 2: Kembangkan for loop ini, 
# supaya huruf yang udah ketebak sebelumnya tetap tercetak di display. 

    for letter in chosen_word:
        if letter == guess:
            ketebak.append(letter)

    display = ""   # ini penting buat tarok di dalam loop while, biar jadi kosong lagi pas ngescan huruf baru
    for letter in chosen_word:
        if letter in ketebak:
            display += letter
        else:
            display += "_"

    print(display)
