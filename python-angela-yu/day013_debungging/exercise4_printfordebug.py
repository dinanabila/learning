jumlah_kata_per_hal = 0
jumlah_hal = int(input("Jumlah halaman: "))
jumlah_kata_per_hal == int(input("Jumlah kata per halaman: "))
total_kata = jumlah_hal * jumlah_kata_per_hal
print(total_kata)

# debug
print("\n====debug====")
print(f"jumlah hal: {jumlah_hal}")
print(f"jumlah kata per hal: {jumlah_kata_per_hal}") # setelah diprint, ternyata bug nya ini

# kenapa tetep 0, si jumlah_kata_per_hal?
# soalnya pakai ==, bukan =