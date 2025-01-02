import random

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# src ascii art: https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for i in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

# TODO 1: Bikin variabel baru, namain lives, buat ngetrack jumlah nyawa yang masih tersisa.
# bikin jadi 6 nyawa buat awal game. 

lives = 6
game_over = False
ketebak = []

while lives > 0 and not game_over:
    guess = input("Tebak huruf (ketik + enter): ").lower()

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

    # TODO 2: bikin kondisi, kalau guess != letter di chosen_word, kurangi lives dengan 1, 
    # terus kalau lives nya udah sampai 0, print 'kamu kalah'. 
    if guess not in chosen_word:
        lives -= 1
    
    if lives == 0:
        print("Hangman")

    # TODO 3: print ASCII art dari list stages sesuai dengan jumlah lives yang masih tersisa.
    # print(stages[lives])
    print(stages[6 - lives])

    if "_" not in display:
        game_over = True
        print("Selamat! Man selamat!")
