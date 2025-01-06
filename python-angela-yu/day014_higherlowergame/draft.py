from game_data import data
from random import choice

# bikin fungsi buat ngecek perbandingan jumlah follower kedua data itu
# outputnya jawaban yang benar (yang punya lebih banyak follower)
def compare_follower(a, b):
    if a['follower_count'] < b['follower_count']:
        return b['name'] # ig2
    elif a['follower_count'] > b['follower_count']:
        return a['name'] # ig1


# bikin fungsi buat ngecek jawaban user bener atau ga
def cek_jawaban(user, benar):
    # bikin kondisional, kalau bener, print current score + lanjut ke soal baru, 
    # kalau salah, print total skor akhir dan hentikan program
    if user != benar:
        print("Ups, bukan itu. Skor akhir: ...")
        return
    elif user == benar:
        print("Benar!")
        print("Skor: ...")


# ambil acak 2 data dari game_data pakai random choice
# jangan sampai data yang diambil sama. harus beda, kan mau dibandingin
# dan, jangan sampai data yang diambil jumlah followernya sama

ig1 = choice(data)
ig2 = ig1
while ig2 == ig1 and ig2['follower_count'] == ig1['follower_count']:
    ig2 = choice(data)


# bikin input jawaban user
jawaban_user = input("Siapa yang followernya lebih banyak? Ketik 'A' atau 'B': ").lower()
# bikin kondisional, kalau 'A', berarti jawaban_user = ig1['name'], 
# kalau 'B', berarti jawaban_user = ig2['name']
if jawaban_user == 'a':
    jawaban_user = ig1['name']
elif jawaban_user == 'b':
    jawaban_user = ig2['name']


jawaban_benar = compare_follower(ig1, ig2)
cek_jawaban(jawaban_user, jawaban_benar)


# === debug ===
print("\n\n======DEBUG======")
print(ig1)
print(ig2)
print(f"Jawaban user: {jawaban_user}")
print(f"Jawaban benar: {jawaban_benar}")
# === debug end ===



