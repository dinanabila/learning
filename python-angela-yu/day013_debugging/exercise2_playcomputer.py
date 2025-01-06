# bayangin jadi komputer kalau mau debug

tahun = int(input("Kamu lahir tahun berapa?: "))

if tahun > 1980 and tahun < 1994:
    print("Kamu millenial")
elif tahun > 1994: # ini harusnya >= 1994
    print("kamu gen z")


# debug: 
# gimana kalau yang input lahirnya <= tahun 1980?
# gimana kalau lahirnya tahun 1994?