# Program buat ngecek bilangan genap / ganjil

angka = int(input("Masukkan angka (dalam bilangan bulat): "))

if angka % 2 == 0:
    print(f"{angka} adalah bilangan genap")
else:
    print(f"{angka} adalah bilangan ganjil")
