from art import blackjack
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
pilihan_aksi = ['pass', 'hand']

def ambil_kartu(banyak_kartu, kartu_siapa):
    '''Ambil kartu acak sebanyak "banyak_kartu" ke tangan "kartu_siapa"'''
    hand = kartu_siapa
    for _ in range(banyak_kartu):
        hand.append(random.choice(cards))
    return hand

def hitung_skor(kartu_siapa):
    '''Hitung skor dari user "kartu_siapa"'''
    if sum(kartu_siapa) == 21 and len(kartu_siapa) == 2:
        return 0
    if sum(kartu_siapa) > 21 and 11 in kartu_siapa:
        kartu_siapa.remove(11)
        kartu_siapa.append(1)
        return sum(kartu_siapa)
    return sum(kartu_siapa)

def keadaan_terakhir():
    '''Print semua kartu di tangan player dan komputer beserta skornya'''
    print(f"    Kartu di tangan kamu: {kartu_pemain}, skor sekarang: {skor_pemain}")
    print(f"    Kartu di tangan komputer: {kartu_komputer}, skor komputer: {skor_komputer}")

print("Hai, aku komputer 'v')/")
print("Mau main satu ronde blackjack sama aku?")

masih_mau_main = True
while masih_mau_main: 
    hand = []
    kartu_pemain = []
    kartu_komputer = []
    pemain_aman = True
    komputer_aman = True
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
        kartu_pemain = ambil_kartu(2, kartu_pemain)
        kartu_komputer = ambil_kartu(2, kartu_komputer)
        skor_pemain = hitung_skor(kartu_pemain)
        skor_komputer = hitung_skor(kartu_komputer)
        print(f"    Kartu di tangan kamu: {kartu_pemain}, skor sekarang: {skor_pemain}")
        print(f"    Kartu pertama komputer: {kartu_komputer[0]}")

        while pemain_aman:
            typo = True
            while typo:
                aksi_pemain = input("\nKetik 'y' kalau mau tambah kartu, ketik 'g' kalau mau pass aja: ").lower()
                if aksi_pemain == 'y' or aksi_pemain == 'g':
                    typo = False
                else:
                    print("Kamu typo. Coba input ulang.")

            if aksi_pemain == 'y':
                kartu_pemain = ambil_kartu(1, kartu_pemain)
                skor_pemain = hitung_skor(kartu_pemain)
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
            elif aksi_pemain == 'g':
                while komputer_aman:
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