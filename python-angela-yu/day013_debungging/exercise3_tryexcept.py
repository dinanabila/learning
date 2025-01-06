# usia = int(input("Berapa usiamu?: ")) 
# ini bakal eror kalau user input str, jadi, kita tambahkan try except

try:
    usia = int(input("Berapa usiamu?: ")) 
except ValueError: # ValueError ini didapet dari eror pas ngerun inputan str
    print("Kamu ga ngetik angka. Coba lagi masukkan angka numerik, bukan dalam bentuk kata / huruf")
    usia = int(input("Berapa usiamu?: ")) 

if usia > 18:
    print("Kamu udah boleh nyetir di usia {usia}") # ini tipe bug yang mengandalkan exp pemrogram. 
    # Kalau ga tau f, bakal hah hoh hah hoh, kecuali nanya gpt. enak si skrng ada gpt