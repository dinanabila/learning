from art import kalkulator

def jumlah(n1, n2):
    return n1 + n2

def kurang(n1, n2):
    return n1 - n2

def kali(n1, n2):
    return n1 * n2

def bagi(n1, n2):
    return n1 / n2

# TODO: Masukin keempat fungsi di atas ke dalam satu dictionary sebagai values. 
# Keys = "+", "-", "*", "/"

operasi = {
    "+": jumlah,
    "-": kurang,
    "*": kali,
    "/": bagi,
}

# # TODO: Cobain operasinya dari dictionary operasi
# print(operasi["+"](2, 4))
kalkulator_hidup = True
while kalkulator_hidup:
    print(kalkulator)
    hasil = 0
    lanjut = True
    a = float(input("Angka pertama: "))
    while lanjut:
        # print("+\n-\n*\n/")
        # ========
        # ANGELA'S
        # ========
        # aku ga kepikiran buat ngambil key aja dari dictionary operasi, 
        # jadi manual print aja tadinya
        for key in operasi:
            print(key)
        # ============
        # END ANGELA'S
        # ============

        hitung = input("Operasi: ")
        b = float(input("Angka kedua: "))
        hasil = operasi[hitung](a, b)
        print(f"{a} {hitung} {b} = {hasil}")
        lanjut_hitungan = input("Ketik 'y' kalau mau lanjutin hitungan ini. \nKetik 'n' kalau mau ngitung hitungan baru. \nKetik 'z' kalau mau matiin kalkulator \nInput: ").lower()
        
        if lanjut_hitungan == 'y':
            a = hasil
        elif lanjut_hitungan == 'n':
            print("\n" * 100)
            lanjut = False
        elif lanjut_hitungan == 'z':
            print("Sampai jumpa")
            lanjut = False
            kalkulator_hidup = False

# ========
# ANGELA's
# ========
# Angela ga pakai while loop lagi buat matiin kalkulator.
# (sementara aku pakai while kalkulator_hidup)
# Jadi simply seluruh programnya jadiin fungsi aja, namain kalkulator().
# User tinggal matiin aja programnya kalau memang mau udahan. 