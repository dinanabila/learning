print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
choice = input("Type 'left' or 'right': ").lower()

if choice == 'right':
    print('\nYou happened to run into your mom and were immediately taken home. Game over.\n')
elif choice == 'left':
    print("\nYou see a river. There's a crocodile, too, there, seeing directly into your eyes. Better swim, or wait him to go?")
    choice = input("Type 'swim' or 'wait': ").lower()
    if choice == 'swim':
        print('\nThe crocodile enjoy his nice dinner tonight. Game over.\n')
    elif choice == 'wait':
        print('\nThe crocodile find his female friend swimming on another side of river, and he suddenly gone from your sight. You can swim safely now.')
        print('Now you found three doors. Which one will you choose? Red, Yellow, or Blue?')
        choice = input("Type 'red' or 'yellow' or 'blue': ").lower()
        if choice == 'red':
            print("\nIt's an empty room, and suddenly you're locked out by someone and can't get out. Game over.\n")
        elif choice == 'blue':
            print("\nIt's an empty room, and suddenly you're locked out by someone and can't get out. Game over.\n")
        elif choice == 'yellow':
            print("\nCongratulations! You've found your treasure \(^v^)/\n")
        else:
            print("\nYou’re stuck in a void because you didn’t choose 'red' or 'yellow' or 'blue' (typo input).\n")
    else:
        print("\nYou’re stuck in a void because you didn’t choose 'swim' or 'wait' (typo input).\n")
else:
    print("\nYou’re stuck in a void because you didn’t choose 'left' or 'right' (typo input).\n")
