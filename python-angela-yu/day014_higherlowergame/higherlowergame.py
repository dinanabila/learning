from game_data import data
from random import choice
from art import logo, vs

def compare_follower(a, b):
    '''input: jumlah follower kedua akun. output: nama akun yang followernya lebih banyak'''
    if a['follower_count'] < b['follower_count']:
        return b['name'] 
    elif a['follower_count'] > b['follower_count']:
        return a['name'] 


def cek_jawaban(user, benar, skor):
    '''input: jawaban user, jawaban benar, sama skor. return skor'''
    if user != benar:
        print("\n" * 100)
        print(art.logo)
        print(f"Ups, bukan {user}. Skor akhir: {skor}")
        return
    elif user == benar:
        print("\n" * 100)
        print(logo)
        skor += 1
        print(f"Benar!                  Skor: {skor}\n")
        return skor


def higher_lower_game():
    masih_mau_main = True
    while masih_mau_main:
        print(logo)
        jumlah_skor = 0
        jawaban_benar = None
        jawaban_user = None
        while jawaban_user == jawaban_benar: 
            ig1 = choice(data)
            ig2 = ig1
            while ig2 == ig1 and ig2['follower_count'] == ig1['follower_count']:
                ig2 = choice(data)

            print(f"A: {ig1['name']}, {ig1['description']} di {ig1['country']}")
            print(vs)
            print(f"\nB: {ig2['name']}, {ig2['description']} di {ig2['country']}")

            jawaban_user = input("\nSiapa yang followernya lebih banyak? Ketik 'A' atau 'B': ").lower()

            if jawaban_user == 'a':
                jawaban_user = ig1['name']
            elif jawaban_user == 'b':
                jawaban_user = ig2['name']

            jawaban_benar = compare_follower(ig1, ig2)
            jumlah_skor = cek_jawaban(jawaban_user, jawaban_benar, jumlah_skor)

        typo = True
        while typo:
            lagi_atau_ga = input("\nMau main lagi? Ketik 'y' kalau mau, 'g' kalau udahan: ")
            if lagi_atau_ga == 'g' or lagi_atau_ga == 'y':
                if lagi_atau_ga == 'g':
                    print("Ok, see ya! ( 'v')/")
                    masih_mau_main = False
                else:
                    print("\n" * 100)
                typo = False
            else:
                print("Ups, kamu typo. Coba lagi.")


higher_lower_game()
