from game_data import data
from random import choice
import art

# bikin fungsi buat ngecek perbandingan jumlah follower kedua data itu
# outputnya jawaban yang benar (yang punya lebih banyak follower)
def compare_follower(a, b):
    '''input: jumlah follower kedua akun. output: nama akun yang followernya lebih banyak'''
    if a['follower_count'] < b['follower_count']:
        return b['name'] # ig2
    elif a['follower_count'] > b['follower_count']:
        return a['name'] # ig1


# bikin fungsi buat ngecek jawaban user bener atau ga
def cek_jawaban(user, benar, skor):
    '''input: jawaban user, jawaban benar, sama skor. return skor'''
    # bikin kondisional, kalau bener, print current score + lanjut ke soal baru, 
    # kalau salah, print total skor akhir dan hentikan program
    if user != benar:
        print("\n" * 100)
        print(art.logo)
        print(f"Ups, bukan {user}. Skor akhir: {skor}")
        return
    elif user == benar:
        print("\n" * 100)
        print(art.logo)
        skor += 1
        print(f"Benar!                  Skor: {skor}\n")
        return skor

def higher_lower_game():
    # bikin while loop masih_mau_main()
    masih_mau_main = True
    while masih_mau_main:
        print(art.logo)
        jumlah_skor = 0
        jawaban_benar = None
        jawaban_user = None
        while jawaban_user == jawaban_benar: 
            # ambil acak 2 data dari game_data pakai random choice
            # jangan sampai data yang diambil sama. harus beda, kan mau dibandingin
            # dan, jangan sampai data yang diambil jumlah followernya sama
            ig1 = choice(data)
            ig2 = ig1
            while ig2 == ig1 and ig2['follower_count'] == ig1['follower_count']:
                ig2 = choice(data)

            # bikin soal
            print(f"A: {ig1['name']}, {ig1['description']} di {ig1['country']}")
            print(art.vs)
            print(f"\nB: {ig2['name']}, {ig2['description']} di {ig2['country']}")

            # bikin input jawaban user
            jawaban_user = input("\nSiapa yang followernya lebih banyak? Ketik 'A' atau 'B': ").lower()
            # bikin kondisional, kalau 'A', berarti jawaban_user = ig1['name'], 
            # kalau 'B', berarti jawaban_user = ig2['name']
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

            

        


    # === debug ===
    print("\n======DEBUG======")
    print(ig1)
    print(ig2)
    print(f"Jawaban user: {jawaban_user}")
    print(f"Jawaban benar: {jawaban_benar}")
    # === debug end ===

higher_lower_game()
