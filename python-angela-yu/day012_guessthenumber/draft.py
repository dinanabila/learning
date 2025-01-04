import random
from art import logo

# TODO 9: bikin fungsi tebak_angka()
def tebak_angka():

    # TODO 8: bikin fungsi compare nyawa
    def compare_nyawa(alat_loop):
        if nyawa == 0:
            print("Yah, sisa kesempatanmu udah habis.")
            print(f"\n******* ANGKA YANG BENAR: {yang_benar} *******")
            return False
        else:
            print("Coba tebak lagi")
            print(f"\n******* TERSISA {nyawa} KESEMPATAN LAGI *******")
            return True

    # TODO 7: susun todo 1 - 6
    # TODO 3: print selamat datang
    print(logo)
    print("\nHaii, ayo main tebak-tebakan angka!\nDari angka 1 - 100, coba tebak, angka apa yang kupikirkan?")
    # TODO 2: bikin angka random 1 - 100, masukin ke variabel
    yang_benar = random.randint(1, 100)
    print(yang_benar)
    print("Tapi sebelum itu, biar lebih menantang, kita bakal batasi jumlah tebakan yang bisa kamu tebak.")
    print("\nKamu mau mode gampang (boleh 10 kali nebak), atau susah (cuma bisa 5 kali nebak)? ")

    # TODO 4: bikin kondisional pilihan mode nyawa
    typo = True
    nyawa = 0
    while typo: 
        mode = input("\nKetik 'a' kalau mau gampang, 'b' kalau mau susah: ").lower()
        if mode == 'a': 
            nyawa = 10
            typo = False
        elif mode == 'b':
            nyawa = 5
            typo = False
        else:
            print("Kamu typo. Coba ketik ulang ('a' atau 'b')")

    # TODO 6: bikin loop game masih jalan
    not_game_over = True
    while not_game_over: 
        # TODO 1: bikin input yang diperlukan
        angka_tebakan = int(input("\nKetik angka tebakanmu: "))
        # eh, ini doang keknya o_o
        # oh sama pilihan easy / hard mode

        # TODO 5: bikin kondisional game
        if angka_tebakan == yang_benar:
            print("Tebakanmu benar! :D")
            not_game_over = False
        elif angka_tebakan < yang_benar:
            nyawa -= 1
            print("Masih kerendahan")
            not_game_over = compare_nyawa(not_game_over)
        else:
            nyawa -= 1
            print("Masih ketinggian")
            not_game_over = compare_nyawa(not_game_over)

mau_main = True
while mau_main:
    typo = True
    while typo: 
        yuk = input("\nMau main tebak angka sama aku? Ketik 'y' kalau iya, 'g' kalau ngga: ").lower()
        if yuk != 'y' and yuk != 'g':
            print("Typo. Coba ketik lagi ('y' atau 'g')")
        else:
            typo = False

    if yuk == 'g':
        print("Ok. See ya ( 'v')/")
        mau_main = False
    else:
        tebak_angka()