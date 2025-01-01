from art import gavel
print(gavel)


print("\nSELAMAT DATANG DI SECRET AUCTION\n")

def secret_auction(nama_bidder, besar_bid):
    print(f"Pemenangnya: {nama_bidder}")

orang_selanjutnya = "ya"
while orang_selanjutnya == "ya":
    nama = input("Nama: ")
    bid = input("Jumlah bid: ")
    orang_selanjutnya = input("Masih ada yang mau nge-bid? (ketik 'ya' kalau masih): ").lower()

    print("\n" * 100)

    if orang_selanjutnya != "ya":
        secret_auction(nama, bid)
    