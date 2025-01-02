import random
import hangman_words
import hangman_art

word_list = hangman_words.word_list

stages = hangman_art.stages

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
    print(f"************************KAMU MASIH PUNYA {lives} NYAWA************************")
    guess = input("Tebak huruf (ketik + enter): ").lower()

    if guess not in chosen_word:
        lives -= 1
        print("Ups. Bukan itu hurufnya.")

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
        print(f"************** yang benar '{chosen_word}'. hangman! **************")

    print(stages[6 - lives])

    if "_" not in display:
        game_over = True
        print("*******************SELAMAT! MAN SELAMAT!*******************")