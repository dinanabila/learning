from art import gavel
print(gavel)

print("\nSELAMAT DATANG DI SECRET AUCTION\n")

# ========
# KOTRETAN
# ========
# loop yang diperlukan: 
# sisir setiap jumlah_bid dari dict auction
# pakai kondisional, kalau max, ambil jumlah_bid itu
# lalu ambil nama_bidder yang punya jumlah_bid itu. 

# pertanyaannya: gimana kalau ada yang jumlah bid max nya sama? 
# kalau kayak gitu, kita tetep print nama_biddernya yang menang, 
# biar mereka ulang auctionnya sendiri lagi di program yang sama
# ============
# KOTRETAN END
# ============

def secret_auction(auction):
    max_bid = 0
    pemenang = ""
    # ==========
    # VERSI ACUU
    # ==========
    # for i in auction:
    #     if auction[i] > max_bid:
    #         max_bid = auction[i]
    
    # for key, value in auction.items():
    #     if value  == max_bid:
    #         pemenang += " " + key
    # ==============
    # END VERSI ACUU
    # ==============

    # ============
    # VERSI ANGELA
    # ============
    for i in auction:
        if auction[i] > max_bid:
            max_bid = auction[i]
    pemenang += " " + i
    # ================
    # END VERSI ANGELA
    # ================
    print("\nList semua bid:")
    for key, value in auction.items():
        print(f"{key}: Rp{value}")
    print("\n")
    print(f"Pemenangnya{pemenang} dengan bid Rp{value}")

auction = {}
orang_selanjutnya = "ya"
lanjut_bidding = True

while lanjut_bidding:
    nama = input("Nama: ")
    bid = int(input("Jumlah bid: Rp"))
    orang_selanjutnya = input("Masih ada yang mau nge-bid? (ketik 'ya' kalau masih): ").lower()

    auction[nama] = bid

    if orang_selanjutnya != "ya":
        lanjut_bidding = False
        secret_auction(auction)
    elif orang_selanjutnya == 'ya':
        print("\n" * 100)
    