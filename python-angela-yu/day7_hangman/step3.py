import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for i in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

ketebak = [] # ini harus tarok di luar loop, supaya ga jadi kosong lagi pas loop nya balik ke awal

# ============
# VERSI KELIRU
# ============
# # TODO 1: Bikin while loop supaya user bisa nebak huruf lagi. 
# while "_" in placeholder:
#     guess = input("Tebak huruf (ketik + enter): ").lower()

# # TODO 2: Kembangkan for loop ini, 
# # supaya huruf yang udah ketebak sebelumnya tetap tercetak di display. 
#     display = ""
#     for letter in chosen_word:
#         if letter == guess:
#             ketebak.append(letter)

#     display = ""   # ini penting buat tarok di dalam loop while, biar jadi kosong lagi pas ngescan huruf baru
#     for letter in chosen_word:
#         if letter in ketebak:
#             display += letter
#         else:
#             display += "_"

#     print(display)

# =====================
# NYOBAIN SOLUSI ANGELA
# =====================
# perbedaan yang ke-notice:
# angela bikin kondisi game_over. aku belum. 
# di sini aku sadar kalau aku udah bikin infinite loop. 
# soalnya while nya pakai placeholder, yaiyalah bakal selalu ngeloop o_o
# angela append letter nya disatuin sama for sebelumnya. aku dipisah.
# dan karena append nya ditarok di dalam if di for itu, jadinya tambahin elif baru. 

# VERSI ANGELA:
game_over = False # janlup definisiin variabel game_over
# TODO 1: Bikin while loop supaya user bisa nebak huruf lagi. 
while not game_over:
    guess = input("Tebak huruf (ketik + enter): ").lower()

# TODO 2: Kembangkan for loop ini, 
# supaya huruf yang udah ketebak sebelumnya tetap tercetak di display. 
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            ketebak.append(letter)
        elif letter in ketebak:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("Kamu menang!")
