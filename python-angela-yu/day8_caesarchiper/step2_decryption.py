alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# tujuan = input("Ketik 'encode' untuk mengenkripsi pesan, 'decode' untuk mendekripsi pesan: ").lower()
pesan = input("\nKetik pesanmu: ").lower()
shift = int(input("\nKetik kode angka rahasiamu: "))

def enkripsi(pesan_awal, banyak_loncatan):
    hasil =""
    for huruf in pesan_awal:
        if huruf == " ":
            hasil += " "
        else:
            hasil += alphabet[(alphabet.index(huruf) + banyak_loncatan) % len(alphabet)]
    
    print(hasil)

enkripsi(pesan, shift)


# TODO 1: Bikin fungsi dekripsi(), yang inputnya pesan_awal dan banyak_loncatan

# TODO 2: Susun perintah yang bikin huruf-huruf di dalam pesan_awal mundur sebanyak banyak_loncatan

# TODO 3: Kombinasikan fungsi enkripsi() dan dekripsi() ke dalam satu fungsi: caesar()
# Pakai nilai dari variable 'direction' buat nentuin program, pakai dekripsi, atau enkripsi