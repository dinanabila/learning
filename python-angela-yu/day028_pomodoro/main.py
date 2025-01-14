from tkinter import *
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0 # untuk penanda kapan 25/5/15 timer nya nyala
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer", fg=GREEN)
    label_ceklis.config(text="")








# ---------------------------- TIMER MECHANISM ------------------------------- # 

def mulai_timer():
    global reps
    # durasi_gawe = WORK_MIN * 60
    # durasi_istirahat_bentar = SHORT_BREAK_MIN * 60
    # durasi_istirahat_lama = LONG_BREAK_MIN * 60

    # buat ngetes timer
    durasi_gawe = 10
    durasi_istirahat_bentar = 3
    durasi_istirahat_lama = 5

    reps += 1

    # ==============
    # PERCOBAAN AWAL
    # ==============
    # # untuk rep ke-1/3/5/7, hitungan timer nya pakai durasi_gawe
    # if reps in range(1, 8, 2):
    #     hitung_mundur(durasi_gawe)

    # # untuk rep ke-8, hitungan timer nya pakai durasi_istirahat_lama
    # if reps == 8:
    #     hitung_mundur(durasi_istirahat_lama)

    # # untuk rep ke-2/4/6, hitungan timer nya pakai durasi_istirahat_bentar
    # if reps in range(2, 7, 2):
    #     hitung_mundur(durasi_istirahat_bentar)

    # if reps > 8:
    #     reps = 0

    # =============
    # END PERCOBAAN
    # =============

    # =============
    # SOLUSI ANGELA
    # =============

    if reps % 8 == 0:
        hitung_mundur(durasi_istirahat_lama)
        label_timer.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        hitung_mundur(durasi_istirahat_bentar)
        label_timer.config(text="Break", fg=PINK)
    else:
        hitung_mundur(durasi_gawe)
        label_timer.config(text="Gawe", fg=GREEN)

    # =================
    # END SOLUSI ANGELA
    # =================

    # ============
    # BUG DETECTED
    # ============
    # sama kayak percobaan awal, pakai solusi angela bug nya masih sama, 
    # kalau kita klik start padahal timernya masih jalan, 
    # timer angka hitung mundurnya bakal saling nimpa


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def hitung_mundur(hitungan):

    hitungan_menit = math.floor(hitungan / 60)
    hitungan_detik = hitungan % 60

    if len(str(hitungan_detik)) == 1:
        hitungan_detik = f"0{hitungan_detik}"

    canvas.itemconfig(timer_text, text=f"{hitungan_menit}:{hitungan_detik}")
    if hitungan > 0:
        global timer
        timer = window.after(1000, hitung_mundur, hitungan - 1)
    else: 
        mulai_timer()
        # if reps % 2 == 0:
            # ceklis = "✔" * int(reps/2)
            # label_ceklis.config(text=ceklis)
            # ga bisa ini kalau pakai float 
        # solusi angela:
        semua_ceklis = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            semua_ceklis += "✔"
        label_ceklis.config(text=semua_ceklis)
            

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



# # belajar after nya tkinter buat bikin timer

# # setelah 1000ms aka 1 detik, print tes
# def tes_aja(tes):
#     print(tes)

# window.after(1000, tes_aja) # (waktu_dalam_ms, nama_fungsi, argumen untuk fungsinya)



# ======
# LAYOUT
# ======

# kita pakai grid layout (row, col)
# 0,0     0,1     0,2
# 1,0     1,1     1,2
# 2,0     2,1     2,2
# 3,0     3,1     3,2

# =======================================================
# BIKIN CANVAS GAMBAR TOMAT SAMA TIMER 00:00 (GRID (1,1))
# =======================================================

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) # width dan height dalam px
tomato_img = PhotoImage(file="day028_pomodoro/tomato.png")
canvas.create_image(100, 112, image=tomato_img) # (koor_x, koor_y, image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


# ==============================
# BIKIN LABEL TIMER (GRID (0,1))
# ==============================

label_timer = Label(text="Timer", fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 35, "bold"), pady=10)
label_timer.grid(row=0, column=1)


# ===============================
# BIKIN LABEL CEKLIS (GRID (3,1))
# ===============================
label_ceklis = Label(text="", fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 20, "bold"), pady=10)
label_ceklis.grid(row=3, column=1)


# ===============================
# BIKIN TOMBOL START (GRID (2,0))
# ===============================
tombol_start = Button(text="Start", command=mulai_timer, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 15, "bold"))
tombol_start.grid(row=2, column=0)


# ===============================
# BIKIN TOMBOL RESET (GRID (2,2))
# ===============================
tombol_reset = Button(text="Reset", command=reset_timer, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 15, "bold"))
tombol_reset.grid(row=2, column=2)


window.mainloop()


# note:
# untuk nanti-nanti kalau balik lagi ke sini, 
# tinjau line 90
# nanti coba di-solve
