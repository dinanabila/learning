import random

word_list = ["aardvark", "baboon", "camel"]

# TODO 1: ambil acak word dari list word_list, 
# terus masukin ke variable chosen_word. Print.
chosen_word = random.choice(word_list)
print(chosen_word)

# TODO 2: minta user tebak satu huruf (input), 
# terus masukin ke variable guess. Bikin lowercase.
guess = input("Tebak huruf (ketik + enter): ").lower()

# TODO 3: cek, huruf di guess itu ada di chosen_word atau ga. 
# Print "Right" kalau iya. "Wrong" kalau ngga. 

# ini aku search google dulu, ketemu method str: __contains__()
# if chosen_word.__contains__(guess):
#     print("Right")
# else:
#     print("False")
# tapi ternyata bukan ini yang outputnya diperlukan

# solusi yang sebenarnya:
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
