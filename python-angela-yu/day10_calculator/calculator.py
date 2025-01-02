def jumlah(n1, n2):
    return n1 + n2

# TODO: Bikin fungsi kurang, kali, bagi

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

# TODO: Cobain operasinya dari dictionary operasi
print(operasi["+"](2, 4))