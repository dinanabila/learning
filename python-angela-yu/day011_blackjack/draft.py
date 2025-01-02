# program blackjack

# aturan house:
# 1. deck unlimited
# 2. ga ada joker
# 3. j/q/k dianggap 10
# 4. as dianggap 11
# 5. deck: cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# 6. peluang terambilnya setiap kartu adalah sama
# 7. dealer: komputer

from art import blackjack
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
hand = []

def first_hand():
    for kartu in range(3):
        kartu = random.choice(cards)
        hand.append(kartu)
    return hand

# main_lagi = input("Hai, aku komputer. \nMau main satu ronde blackjack sama aku? \nKetik 'y' kalau mau, 'g' kalau ga: ").lower()
# print(blackjack)
# aksi = input("Ketik 'y' kalau mau tambah kartu, ketik 'g' kalau mau pass aja: ").lower()


# TODO: bikin first card pemain dan komputer pakai random
kartu_perdana_pemain = first_hand()
kartu_perdana_komputer = first_hand()

print(f"komputer first hand: {kartu_perdana_komputer}")
print(f"first hand pemain: {kartu_perdana_pemain}")

