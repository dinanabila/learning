alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# tujuan = input("Ketik 'encode' untuk mengenkripsi pesan, 'decode' untuk mendekripsi pesan: ").lower()
pesan = input("\nKetik pesanmu: ").lower()
shift = int(input("\nKetik kode angka rahasiamu: "))

# ===========================
# VERSI ACUU YANG RADA KELIRU
# ===========================

# ========
# KOTRETAN
# ========
# ini kita dikasih list alphabet, pasti gunanya buat gerakin huruf pakai shift, manfaatin fitur index list
# berarti, si input pesan nya harus bisa kita kaitin sama alphabet?
# tapi gimana caranya?
# a index 0, b index 1, c index 2, dst
# cek str satu per satu di variabel pesan
# if str di pesan == alphabet[i]: str = alphabet[i + shift]

# cobain ini dulu biar kebayang cara kerja str dan index
# teks = "apple"
# print(teks[1])
# for i in range(len(teks)):
#     print(teks[i])

# begitupula dengan list
# for huruf in range(len(alphabet)):
#     print(alphabet[huruf])
# ============
# KOTRETAN END
# ============

# # TODO 1: Bikin fungsi enkripsi(), buat ngambil pesan dan shift sebagai input
# def enkripsi(pesan, shift):

#     # TODO 2: Di dalam fungsi enkripsi(), tulis perintah yang bikin huruf-huruf di teks 
#     # kegeser sebanyak shift langkah, lalu print hasil enkripsinya
#     hasil = ""
#     for i in range(len(pesan)):
#         if pesan[i] == " ":
#             hasil += " "
#         for j in range(len(alphabet)):
#             if pesan[i] == alphabet[j]:
#                 # TODO 4: Atasi problem geser z biar bisa kegeser ke a dst
#                 # ========
#                 # KOTRETAN
#                 # ========
#                 # initu pakai mod gasi
#                 # jadi misalkan list kita [0, 1]
#                 # berarti index 2 = index 0, index 3 = index 1, 4 = 0, 5 = 1, dst
#                 # mod 2 itu, a.k.a mod(len(listnya))
#                 # 2 = 2 mod 2 = 0, 3 = 3 mod 2 = 1, dst
#                 # ============
#                 # KOTRETAN END
#                 # ============
                
#                 # hasil += alphabet[j + shift] --> tadinya kodenya ini sebelum todo 4
#                 hasil += alphabet[(j + shift) % len(alphabet)]

#     print(hasil)

# # TODO 3: Call fungsi enkripsi() dan pass in input dari user
# enkripsi(pesan, shift)

# =================
# END VERSI ACUU ;)
# =================

# *********************

# =====================
# NYOBAIN SOLUSI ANGELA
# =====================
# Ternyata ada cara yang lebih simpel: pakai fungsi index() nya list :)))))))
# aku malah manual for satu-satu dicek per alfabet WK
# oh ya, sama, yang perlu dicatat:
# nama parameter itu seingetku harus beda sama variabel input, 
# jadi bener angela

# TODO 1: Bikin fungsi enkripsi(), buat ngambil pesan dan shift sebagai input
def enkripsi(pesan_awal, banyak_loncatan):
    # TODO 2: Di dalam fungsi enkripsi(), tulis perintah yang bikin huruf-huruf di teks 
    # kegeser sebanyak shift langkah, lalu print hasil enkripsinya
    hasil =""
    for huruf in pesan_awal:
        if huruf == " ":
            hasil += " "
        else:
            # TODO 4: Atasi problem geser z biar bisa kegeser ke a dst
            hasil += alphabet[(alphabet.index(huruf) + banyak_loncatan) % len(alphabet)]
    
    print(hasil)

# TODO 3: Call fungsi enkripsi() dan pass in input dari user
enkripsi(pesan, shift)