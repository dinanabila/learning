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

# MESIN: input mode, output nyawa
def genset_nyawa(mode_apa):
    if mode_apa == 'a':
        return GAMPANG
    else:
        return SUSAH

# MESIN: input nyawa dan tebakan, output keputusan
# def tebakan()


# ALUR KESELURUHAN
# START: opening
print(logo)
print("\nHaii, ayo main tebak-tebakan angka!\nDari angka 1 - 100, coba tebak, angka apa yang kupikirkan?")
yang_benar = random.randint(1, 100)
print(f"ini contekan yang bener buat debugging: {yang_benar}")
print("Tapi sebelum itu, biar lebih menantang, kita bakal batasi jumlah tebakan yang bisa kamu tebak.")
print("\nKamu mau mode gampang (boleh 10 kali nebak), atau susah (cuma bisa 5 kali nebak)? ")

# INPUT MODE
mode = input("\nKetik 'a' kalau mau gampang, 'b' kalau mau susah: ").lower()

nyawa = genset_nyawa(mode)
print(nyawa)
