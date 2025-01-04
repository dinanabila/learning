import random
from art import logo

# TODO 1: bikin input yang diperlukan
angka_tebakan = input("Ketik angka tebakanmu: ")
# eh, ini doang keknya o_o
# oh sama pilihan easy / hard mode

# TODO 2: bikin angka random 1 - 100, masukin ke variabel
yang_benar = random.randint(1, 100)

# TODO 3: print selamat datang
print(logo)
print("\nHaii, ayo main tebak-tebakan angka. Dari angka 1 - 100, coba tebak, angka apa yang kupikirkan?")
print("\nTapi sebelum itu, biar lebih menantang, kita batasi jumlah tebakan yang bisa kamu tebak.")
print("\nKamu mau mode gampang (boleh 10 kali nebak), atau susah (cuma bisa 5 kali nebak)? ")
mode = input("Ketik 'a' kalau mau gampang, 'b' kalau mau susah: ")

# TODO 4: bikin kondisional pilihan mode nyawa
typo = True
while typo: 
    if mode == 'a': 
        nyawa = 10
    elif mode == 'b':
        nyawa = 5
    else:
        print("Kamu typo. Coba ketik ulang ('a' atau 'b')")
        typo = False

# TODO 5: bikin kondisional game
if angka_tebakan == yang_benar:
    print("Tebakanmu benar! :D")
elif angka_tebakan < yang_benar:
    print("Masih kerendahan")
else:
    print("Masih ketinggian")

# TODO 6: bikin loop nyawa masih ada
masih_hidup = True
while masih_hidup: 
    if nyawa == 0:
        masih_hidup = False
    else:
        print("Coba tebak lagi")
