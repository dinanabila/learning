from tkinter import *

FONT = ("Arial", 12, "bold")
FONT_ANGKA = ("Arial", 12, "normal")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=5, pady=5)


# ======
# LAYOUT
# ======

# kita pakai layout grid (row, col)
# 0,0   0,1   0,2
# 1,0   1,1   1,2
# 2,0   2,1   2,2


# ============================
# BIKIN LABEL MILES (GRID 0,2)
# ============================

label_miles = Label(text="Miles", font=FONT, padx=10, pady=10)
label_miles.grid(row=0, column=2)


# =========================
# BIKIN LABEL KM (GRID 1,2)
# =========================

label_km = Label(text="Km", font=FONT, padx=10, pady=10)
label_km.grid(row=1, column=2)


# ==================================
# BIKIN LABEL IS EQUAL TO (GRID 1,0)
# ==================================

label_isequalto = Label(text="is equal to", font=FONT, padx=10, pady=10)
label_isequalto.grid(row=1, column=0)


# ==============================================
# BIKIN LABEL HASIL KONVERSI DALAM KM (GRID 1,1)
# ==============================================

label_hasilkonversi = Label(text="0", font=FONT_ANGKA, padx=10, pady=10)
label_hasilkonversi.grid(row=1, column=1)


# =====================
# BIKIN FUNGSI KONVERSI
# =====================

def konversi():
    angka_miles = float(float(input.get()) * 1.6)

    label_hasilkonversi.config(text=angka_miles)


# =================================
# BIKIN TOMBOL CALCULATE (GRID 2,1)
# =================================

tombol_calculate = Button(text="Calculate", command=konversi, font=FONT, padx=10, pady=10)
tombol_calculate.grid(row=2, column=1)



# ============================
# BIKIN ENTRY MILES (GRID 0,1)
# ============================

input = Entry(text="0", width=5, font=FONT_ANGKA)
input.grid(row=0, column=1)

# biar tetep tampil di layar, ga langsung exit:
window.mainloop()