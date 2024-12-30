import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

# TODO 1: Bikin variabel str kosong, namain "placeholder". 
# Isi placeholder dengan _ berdasarkan setiap huruf di chosen_word. 
placeholder = ""
for i in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

# TODO 2: Bikin variabel str kosong, namain "display". 
# display ini isinya placeholder yang udah diisi huruf tebakan user.
guess = input("Tebak huruf (ketik + enter): ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

display = ""
for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)
