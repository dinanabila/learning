import random
import hangman_words
import hangman_art

# TODO 1: update word_list pakai word_list di hangman_words.py
word_list = hangman_words.word_list

# TODO 2: update stages pakai module hangman_art
stages = hangman_art.stages

# TODO 3: print logo hangman
print(hangman_art.logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for i in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

lives = 6
game_over = False
ketebak = []
nebak = []

while lives > 0 and not game_over:
    # TODO 6: kasitau user tinggal berapa lagi nyawanya
    print(f"************************KAMU MASIH PUNYA {lives} NYAWA************************")
    guess = input("Tebak huruf (ketik + enter): ").lower()

    if guess not in chosen_word:
        lives -= 1
        # TODO 5: kalau huruf yang ditebak salah, kasitau user
        print("Ups. Bukan itu hurufnya.")

    # TODO 4: kalau misalkan huruf yang ditebak udah pernah ditebak sebelumnya, kasitau user
    if guess in nebak:
        print("Kamu udah nebak huruf ini tadi.")
    
    nebak.append(guess)

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
    
    if lives == 0:
        print("Hangman")

    print(stages[6 - lives])

    if "_" not in display:
        game_over = True
        print("Selamat! Man selamat!")