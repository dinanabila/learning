alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

tujuan = input("Ketik 'enkripsi' untuk mengenkripsi pesan, 'dekripsi' untuk mendekripsi pesan: ").lower()
pesan = input("\nKetik pesanmu: ").lower()
shift = int(input("\nKetik kode angka rahasiamu: "))

def enkripsi(pesan_awal, banyak_loncatan):
    hasil =""
    for huruf in pesan_awal:
        if huruf == " ":
            hasil += " "
        else:
            hasil += alphabet[(alphabet.index(huruf) + banyak_loncatan) % len(alphabet)]
    
    print("hasil: ", hasil)


# TODO 1: Bikin fungsi dekripsi(), yang inputnya pesan_awal dan banyak_loncatan
def dekripsi(pesan_awal, banyak_loncatan):

# TODO 2: Susun perintah yang bikin huruf-huruf di dalam pesan_awal mundur sebanyak banyak_loncatan
    hasil = ""
    for huruf in pesan_awal:
        if huruf == " ":
            hasil += " "
        else:
            hasil += alphabet[(alphabet.index(huruf) - banyak_loncatan) % len(alphabet)]
    print("hasil: ", hasil)

# TODO 3: Kombinasikan fungsi enkripsi() dan dekripsi() ke dalam satu fungsi: caesar()
# Pakai nilai dari variable 'tujuan' buat nentuin program, pakai dekripsi, atau enkripsi
# def caesar(metode):
#     if metode == "enkripsi":
#         enkripsi(pesan, shift)
#     elif metode == "dekripsi":
#         dekripsi(pesan, shift)
#     else:
#         print("Typo di tujuan. Coba lagi (ketik dekripsi / enkripsi)")

# caesar(tujuan)

# ===================
# NYOBA SOLUSI ANGELA
# ===================

# ternyata todo 3 yang dimaksud itu bukan yang kayak aku bikin
# tapi bener-bener nyatuin jadi satu, biar ga repetitif
# bener sih, biar ga berat juga programnya. 
# oke, jadi ini versi benernya:

def caesar(pesan_awal, banyak_loncatan, enkripsi_atau_dekripsi):
    hasil =""
    for huruf in pesan_awal:
        if huruf == " ":
            hasil += " "
        else:
            if enkripsi_atau_dekripsi == 'enkripsi':
                hasil += alphabet[(alphabet.index(huruf) + banyak_loncatan) % len(alphabet)]
            elif enkripsi_atau_dekripsi == 'dekripsi':
                hasil += alphabet[(alphabet.index(huruf) - banyak_loncatan) % len(alphabet)]
            else:
                print("Typo di tujuan. Coba lagi (ketik dekripsi / enkripsi)")
    
    print("hasil:", hasil)

caesar(pesan, shift, tujuan)
