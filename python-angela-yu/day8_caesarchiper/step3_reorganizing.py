# TODO 1: Import dan print logo caesar chiper dari art.py
from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO 2: Bikin cara supaya simbol selain alfabet ga ilang pas dien/dekripsi. 
# Biarin tetep sama kayak gitu aja, ga usah di-shift yang gimana-gimana

def caesar(pesan_awal, banyak_loncatan, enkripsi_atau_dekripsi):
    hasil =""
    for huruf in pesan_awal:     
        if enkripsi_atau_dekripsi == 'enkripsi':
            if huruf == " ":
                huruf += " "
            if huruf not in alphabet:
                hasil += huruf  
            hasil += alphabet[(alphabet.index(huruf) + banyak_loncatan) % len(alphabet)]
        elif enkripsi_atau_dekripsi == 'dekripsi':
            if huruf == " ":
                huruf += " "
            if huruf not in alphabet:
                hasil += huruf 
            hasil += alphabet[(alphabet.index(huruf) - banyak_loncatan) % len(alphabet)]
            print("hasil:", hasil)
        else:
            print("Typo di tujuan. Coba lagi (ketik dekripsi / enkripsi)")

# TODO 3: Bikin programnya restart sesuai keinginan user (tanya user, mau lagi atau udahan?)
lagi = "ya"
while lagi == 'ya':
    tujuan = input("Ketik 'enkripsi' untuk mengenkripsi pesan, 'dekripsi' untuk mendekripsi pesan: ").lower()
    pesan = input("\nKetik pesanmu: ").lower()
    shift = int(input("\nKetik kode angka rahasiamu: "))

    caesar(pesan, shift, tujuan)

    lagi = input("Mau enkripsi / dekripsi pesan lagi? (ya/ga): ").lower()