# program blackjack

# aturan house:
# 1. deck unlimited
# 2. ga ada joker
# 3. j/q/k dianggap 10
# 4. as dianggap 11 (di awal)
# 5. deck: cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# 6. peluang terambilnya setiap kartu adalah sama
# 7. dealer: komputer

from art import blackjack
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# TODO 3: bikin list buat pilihan random komputer: pass / ambil kartu lagi
pilihan_aksi = ['pass', 'hand']

def ambil_kartu(banyak_kartu, kartu_siapa):
    '''Ambil kartu acak sebanyak "banyak_kartu" ke tangan "kartu_siapa"'''
    hand = kartu_siapa
    for _ in range(banyak_kartu):
        hand.append(random.choice(cards))
    return hand

def hitung_skor(kartu_siapa):
    '''Hitung skor dari user "kartu_siapa"'''
    # skor = 0
    # for i in range(len(kartu_siapa)):
    #     skor += kartu_siapa[i]
    # return skor
    # ========
    # ANGELA's
    # ========
    if sum(kartu_siapa) == 21 and len(kartu_siapa) == 2:
        return 0
    if sum(kartu_siapa) > 21 and 11 in kartu_siapa:
        kartu_siapa.remove(11)
        kartu_siapa.append(1)
        return sum(kartu_siapa)
    return sum(kartu_siapa)
    # ============
    # END ANGELA's
    # ============

# TODO 8: bikin fungsi print keadaan terakhir kartu pemain & komputer biar ga redundant
def keadaan_terakhir():
    '''Print semua kartu di tangan player dan komputer beserta skornya'''
    print(f"    Kartu di tangan kamu: {kartu_pemain}, skor sekarang: {skor_pemain}")
    print(f"    Kartu di tangan komputer: {kartu_komputer}, skor komputer: {skor_komputer}")

print("Hai, aku komputer 'v')/")
print("Mau main satu ronde blackjack sama aku?")

# TODO 5: bikin while masih mau main
masih_mau_main = True
while masih_mau_main: 
    hand = []
    kartu_pemain = []
    kartu_komputer = []
    pemain_aman = True
    komputer_aman = True
    # TODO 6: bikin while typo input
    typo = True
    while typo:
        main_lagi = input("Ketik 'y' kalau mau, 'g' kalau ga: ").lower()
        if main_lagi == 'y' or main_lagi == 'g':
            typo = False
        else:
            print("Typo. Coba lagi.")
    if main_lagi == 'y':
        print("\n" * 100)
        print(blackjack)

        # TODO 1: bikin first card pemain dan komputer pakai random
        kartu_pemain = ambil_kartu(2, kartu_pemain)
        kartu_komputer = ambil_kartu(2, kartu_komputer)
        skor_pemain = hitung_skor(kartu_pemain)
        skor_komputer = hitung_skor(kartu_komputer)
        print(f"    Kartu di tangan kamu: {kartu_pemain}, skor sekarang: {skor_pemain}")
        print(f"    Kartu pertama komputer: {kartu_komputer[0]}")

        # TODO 4: bikin while skor_pemain <= 21 dan skor_komputer <= 21
        while pemain_aman:
            # TODO 7: bikin while typo input
            typo = True
            while typo:
                aksi_pemain = input("\nKetik 'y' kalau mau tambah kartu, ketik 'g' kalau mau pass aja: ").lower()
                if aksi_pemain == 'y' or aksi_pemain == 'g':
                    typo = False
                else:
                    print("Kamu typo. Coba input ulang.")

            # TODO 2: susun kondisional if else mentah biar ada gambaran
            if aksi_pemain == 'y':
                kartu_pemain = ambil_kartu(1, kartu_pemain)
                skor_pemain = hitung_skor(kartu_pemain)
                # TODO 9:tambahin kondisi blackjack ke user
                if skor_pemain == 0:
                    keadaan_terakhir()
                    print("Blackjack. Kamu menang :3")
                    pemain_aman = False
                    komputer_aman = False
                elif skor_pemain > 21:
                    keadaan_terakhir()
                    print("Skormu kebablasan. Kamu kalah :(")
                    pemain_aman = False
                    komputer_aman = False
                else:
                    print(f"    Kartu di tangan kamu: {kartu_pemain}, skor sekarang: {skor_pemain}")
                    print(f"    Kartu pertama komputer: {kartu_komputer[0]}")
                    # balik ke input aksi_pemain
                    # bikin loop while <= 21 berarti
            elif aksi_pemain == 'g':
                while komputer_aman:
                    # TODO 10: tambahin kondisi blackjack ke komputer
                    if skor_komputer == 0:
                        keadaan_terakhir()
                        print("Komputer dapet blackjack! Kamu kalah D:")
                        pemain_aman = False
                        komputer_aman = False
                    else:
                        aksi_komputer = random.choice(pilihan_aksi)
                        if aksi_komputer == 'hand': 
                            kartu_komputer = ambil_kartu(1, kartu_komputer)
                            skor_komputer = hitung_skor(kartu_komputer)
                            if skor_komputer > 21:
                                keadaan_terakhir()
                                print("Skor lawan kebablasan. Kamu menang :D")
                                pemain_aman = False
                                komputer_aman = False
                            # else:
                                # balik lagi ke input random aksi_komputer
                                # ini juga loop while <= 21
                        elif aksi_komputer == 'pass':
                            if skor_pemain > skor_komputer:
                                keadaan_terakhir()
                                print("Kamu menang :D")
                                pemain_aman = False
                                komputer_aman = False
                            elif skor_pemain == skor_komputer:
                                keadaan_terakhir()
                                print("Seri")
                                pemain_aman = False
                                komputer_aman = False
                            else:
                                keadaan_terakhir()
                                print("Kamu kalah D:")
                                pemain_aman = False
                                komputer_aman = False
    
    elif main_lagi == 'g':
        print('See ya')
        masih_mau_main = False
    
    print("\nMau main satu ronde blackjack lagi sama aku?")

# ========
# EVALUASI
# ========

# Angela lebih ringkas kodenya, soalnya dia definisiin fungsi play()
# kalau aku kan pakai while, jadi bertele-tele banget :'))

# Angela pakai strategi 17 buat komputer,
# kalau aku pakai random buat gerakin aksi komputer (ambil kartu / pass)

# Ya udahlah, yang penting bisa jalan blackjack nya

# ============
# EVALUASI END
# ============