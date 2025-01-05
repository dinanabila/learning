# melihat draft 1 yang semrawut
# maka
# timbul keinginan untuk
# menghilangkan kebiasaan nulis bertele-tele

# tolong ya, 
# wahai aku, 
# biasakan manfaatin fitur fungsi, 
# juga, biasakan sederhanakan alurnya
# biar ga jorok

# ==============

# di flowchart 2
# aku punya beberapa mesin a.k.a fungsi

# let's try build them

import random
from art import logo

# GLOBAL VARIABLE
GAMPANG = 10
SUSAH = 5

# [MESIN] input: mode, output: nyawa
def genset_nyawa(mode_apa):
    if mode_apa == 'a':
        return GAMPANG
    else:
        return SUSAH

# [MESIN] input: nyawa dan tebakan, output: tebakan
# def nebak(): 
#     return int(input("\nKetik angka tebakanmu: "))
# mesin ini masukin ke dalam loop di mesin tebakan, 
# di variabel tebakan_user

# [MESIN] input: none, output: start / end
def lagi_atau_ga():
    yuk = input("\nMasih mau main tebak angka sama aku? Ketik 'y' kalau iya, 'g' kalau ngga: ").lower()
    if yuk == 'g':
        print("Ok. See ya ( 'v')/")
    else:
        return game_tebak_angka()

# [MESIN] input: nyawa dan tebakan, output: hasil
def hasil(jumlah_nyawa, tebakan_user, yang_benar):
    if jumlah_nyawa == 1 and tebakan_user != yang_benar:
        print("Yah, sisa kesempatanmu udah habis.")
    elif jumlah_nyawa > 0 and tebakan_user == yang_benar:
        print("Selamatt, tebakanmu benar! :D")
    return lagi_atau_ga()
    
# [MESIN] input: nyawa dan tebakan, output: keputusan
def tebakan(jumlah_nyawa, tebakan_user, yang_benar):
    while tebakan_user != yang_benar:
        tebakan_user = int(input("\nKetik angka tebakanmu: "))
        if jumlah_nyawa > 1 and tebakan_user != yang_benar:
            jumlah_nyawa -= 1
            if tebakan_user > yang_benar:
                print("Masih ketinggian")
            else:
                print("Masih kerendahan")
            print("Coba tebak lagi")
            print(f"\n******* TERSISA {jumlah_nyawa} KESEMPATAN LAGI *******")
        else:
            return hasil(jumlah_nyawa, tebakan_user, yang_benar)

def game_tebak_angka():
    angka = random.randint(1, 100)
    print(f"ini contekan yang bener buat debug: {angka}")

    mode = input("\nKetik 'a' kalau mau gampang, 'b' kalau mau susah: ").lower()
    nyawa = genset_nyawa(mode)
    angka_tebakan = None
    tebakan(nyawa, angka_tebakan, angka)

# ALUR KESELURUHAN
# START: opening
print(logo)
print("\nHaii, ayo main tebak-tebakan angka!\nDari angka 1 - 100, coba tebak, angka apa yang kupikirkan?")
print("Tapi sebelum itu, biar lebih menantang, kita bakal batasi jumlah tebakan yang bisa kamu tebak.")
print("\nKamu mau mode gampang (boleh 10 kali nebak), atau susah (cuma bisa 5 kali nebak)? ")

game_tebak_angka()





