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
kartu_pemain = []
kartu_komputer = []

def ambil_kartu(banyak_kartu, kartu_siapa):
    hand = kartu_siapa
    for _ in range(banyak_kartu):
        hand.append(random.choice(cards))
    return hand

def hitung_skor(kartu_siapa):
    skor = 0
    for i in range(len(kartu_siapa)):
        skor += kartu_siapa[i]
    return skor

# main_lagi = input("Hai, aku komputer. \nMau main satu ronde blackjack sama aku? \nKetik 'y' kalau mau, 'g' kalau ga: ").lower()
# print(blackjack)

# TODO 1: bikin first card pemain dan komputer pakai random
kartu_pemain = ambil_kartu(2, kartu_pemain)
kartu_komputer = ambil_kartu(2, kartu_komputer)
skor_pemain = hitung_skor(kartu_pemain)
skor_komputer = hitung_skor(kartu_komputer)
print(f"    Kartu di tangan kamu: {kartu_pemain}, skor sekarang: {skor_pemain}")
print(f"    Kartu pertama komputer: {kartu_komputer[0]}")

aksi_pemain = input("Ketik 'y' kalau mau tambah kartu, ketik 'g' kalau mau pass aja: ").lower()

# TODO 3: bikin list buat pilihan random komputer: pass / ambil kartu lagi
pilihan_aksi = ['pass', 'hand']

# TODO 2: susun kondisional if else mentah biar ada gambaran
if aksi_pemain == 'y':
    kartu_pemain = ambil_kartu(1, kartu_pemain)
    skor_pemain = hitung_skor(kartu_pemain)
    print(f"    Kartu di tangan kamu: {kartu_pemain}, skor sekarang: {skor_pemain}")
    print(f"    Kartu pertama komputer: {kartu_komputer[0]}")
    if skor_pemain > 21:
        print("Skormu kebablasan. Kamu kalah :(")
    else:
        aksi_komputer = random.choice(pilihan_aksi)
        if aksi_komputer == 'pass':
            if skor_pemain > skor_komputer:
                print("Kamu menang :D")
            elif skor_pemain == skor_komputer:
                print("Kamu kalah")
            else:
                print("Seri")
        elif aksi_komputer == 'hand': 
            kartu_komputer = ambil_kartu(1, kartu_komputer)
            skor_komputer = hitung_skor(kartu_komputer)
            if kartu_komputer > 21:
                print("Skor lawan kebablasan. Kamu menang :D")
            # else:
                # balik lagi ke atas
elif aksi_pemain == 'n':
    aksi_komputer = random.choice(pilihan_aksi)
    if aksi_komputer == 'pass':
        if skor_pemain > skor_komputer:
            print("Kamu menang :D")
        elif skor_pemain == skor_komputer:
            print("Kamu kalah")
        else:
            print("Seri")
    elif aksi_komputer == 'hand': 
        kartu_komputer = ambil_kartu(1, kartu_komputer)
        skor_komputer = hitung_skor(kartu_komputer)
        if kartu_komputer > 21:
            print("Skor lawan kebablasan. Kamu menang :D")
        # else:
            # balik lagi ke atas