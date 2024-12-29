import random

gunting = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

batu = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

kertas = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

pose_tangan = [gunting, batu, kertas]

print("Hai, aku komputer. Ayo main gunting batu kertas sama acuu.")
player = input("Silakan ulurkan tanganmu. Gunting, batu, atau kertas?: ").lower()
print("Kamu: ")
if player == 'gunting':
    player = gunting
elif player == 'batu':
    player = batu
elif player == 'kertas':
    player = kertas

print(player)

print("\nKomputer: ")
komputer = random.choice(pose_tangan)
print(komputer)

if player == komputer:
    print("Seri")
elif player == gunting:
    if komputer == kertas:
        print("Kamu menang.")
    else:
        print("Kamu kalah.")
elif player == batu:
    if komputer == gunting:
        print("Kamu menang.")
    else:
        print("Kamu kalah.")
elif player == kertas:
    if komputer == batu:
        print("Kamu menang.")
    else:
        print("Kamu kalah.")
else:
    print("\nMungkin kamu typo. \n")

# src ascii art: https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe
