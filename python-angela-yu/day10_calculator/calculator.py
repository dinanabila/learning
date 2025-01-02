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
        print("+\n-\n*\n/")
        hitung = input("Operasi: ")
        b = float(input("Angka kedua: "))
        a = operasi[hitung](a, b)
        print(f"hasil: {a}")
        lanjut_hitungan = input("Ketik 'y' kalau mau lanjutin hitungan ini. Ketik 'n' kalau mau ngitung hitungan baru: ").lower()
        
        if lanjut_hitungan == 'y':
            lanjut = True
        elif lanjut_hitungan == 'n':
            lanjut = False
    
    if lanjut_hitungan == 'n':
        print("\n" * 100)