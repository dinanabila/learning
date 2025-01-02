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
    index_max_bid = 0
    for i in auction["jumlah_bid"]:
        if i > max_bid:
            max_bid = i
            index_max_bid = auction["jumlah_bid"].index()
            pemenang = auction["nama_bidder"][index_max_bid]
    print(f"Pemenangnya: {pemenang}")

auction = {}

orang_selanjutnya = "ya"

while orang_selanjutnya == "ya":
    nama = input("Nama: ")
    bid = int(input("Jumlah bid: "))
    orang_selanjutnya = input("Masih ada yang mau nge-bid? (ketik 'ya' kalau masih): ").lower()

    auction[nama] = bid

    print("\n" * 100)

    if orang_selanjutnya != "ya":
        # secret_auction(auction)
        print(auction)
    