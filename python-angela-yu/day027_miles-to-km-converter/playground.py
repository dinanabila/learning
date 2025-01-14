# ==============================
# UNLIMITED POSITIONAL ARGUMENTS
# ==============================

# *args ini buat bikin parameter tanpa harus nyebut secara eksplisit detailnya
# cocok buat yang mau masukin argumen banyak banget, atau unlimited juga bisa
# jangan lupa tulis * nya ya, penting
# * ini buat ngumpulin argumen-argumen kita ke dalam satu tuple bernama args

# oh ya, *args ini bisa ditulis *numbers, atau, *terserahlah
# jadi ga wajib "args"
# jadi kalau gitu, tuple nya namanya bukan args lagi, tapi numbers, atau terserahlah

def add(*args):
    total = 0
    for angka in args:
        total += angka
    return total


jumlah = add(1, 2, 2, 3)
print(jumlah)


# ============================
# **KWARGS (KEYWORD ARGUMENTS)
# ============================

# kwargs itu dictionary