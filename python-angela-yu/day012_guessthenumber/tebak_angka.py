import random
from art import logo

# VARIABEL GLOBAL
GAMPANG = 10
SUSAH = 5

# FUNGSI
def game_tebak_angka():
    def genset_nyawa(mode_apa):
        if mode_apa == 'a':
            return GAMPANG
        else:
            return SUSAH

    def lagi_atau_ga():
        yuk = input("\nMasih mau main tebak angka sama aku? Ketik 'y' kalau iya, 'g' kalau ngga: ").lower()
        if yuk == 'g':
            print("Ok. See ya ( 'v')/")
        else:
            return game_tebak_angka()

    def hasil(jumlah_nyawa, tebakan_user, yang_benar):
        if jumlah_nyawa == 1 and tebakan_user != yang_benar:
            print("Yah, sisa kesempatanmu udah habis")
            print(f"Angka yang benar: {yang_benar}")
        elif jumlah_nyawa > 0 and tebakan_user == yang_benar:
            print("Selamatt, tebakanmu benar! :D")
        return lagi_atau_ga()
        
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
            
    angka = random.randint(1, 100)
    mode = input("\nKetik 'a' kalau mau gampang, 'b' kalau mau susah: ").lower()
    nyawa = genset_nyawa(mode)
    angka_tebakan = None
    tebakan(nyawa, angka_tebakan, angka)

# PROGRAM 
print(logo)
print("\nHaii, ayo main tebak-tebakan angka!\nDari angka 1 - 100, coba tebak, angka apa yang kupikirkan?")
print("Tapi sebelum itu, biar lebih menantang, kita bakal batasi jumlah tebakan yang bisa kamu tebak.")
print("\nKamu mau mode gampang (boleh 10 kali nebak), atau susah (cuma bisa 5 kali nebak)? ")

game_tebak_angka()
