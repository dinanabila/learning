from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

# =========================
# STEP 1: BIKIN BADAN SNAKE
# =========================

# caranya:
# bikin 3 turtle, dan posisiin di tengah
# tiap turtle harus dalam bentuk persegi putih
# ukuran default turtle: 20x20

# ~~~~~~~~~~~~~~~~~~~
# percobaan awal acuu
# ~~~~~~~~~~~~~~~~~~~
# koor_x = [-40, -20, 0]
# semua_part_badan = []
# for part_badan_ke in range(0, 3):
#     part_badan = Turtle(shape="square")
#     part_badan.color("white")
#     part_badan.penup()
#     part_badan.goto(x=koor_x[part_badan_ke],y=0)
#     semua_part_badan.append(part_badan)
# ~~~~~~~~~~~~~~~~~~~~~~~
# end percobaan awal acuu
# ~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# pakai versi angela aja, lebih efisien
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
posisi_awal = [(0, 0), (-20, 0), (-40, 0)]
semua_part_badan = []

for posisi in posisi_awal:
    part_badan = Turtle("square")
    part_badan.color("white")
    part_badan.penup()
    part_badan.goto(posisi)
    semua_part_badan.append(part_badan)


# =========================================
# STEP 3: BIKIN ULARNYA JADI BISA DIKONTROL
# =========================================

# screen.listen()
# screen.onkey(fun = ular.ke_atas, key = "Up")
# screen.onkey(fun = ular.ke_bawah, key = "Down")
# screen.onkey(fun = ular.ke_kanan, key = "Right")
# screen.onkey(fun = ular.ke_kiri, key = "Left")

# run di main.py aja
# di sini ga terintegrasi sama class dari file lain

# =====================================
# STEP 2: BIKIN SNAKE-NYA JALAN SENDIRI
# =====================================

masih_hidup = True
while masih_hidup:
    screen.update()
    # screen.update() ini buat update tampilan pergerakan baru di screen nya
    # soalnya di atas udah di-setting screen.tracer(0)
    # jadi setiap ada pergerakan baru, screen nya harus di-update

    time.sleep(0.1) # 0.1 detik, ini biar snake nya ga kecepetan larinya
    for part_ke in range(len(semua_part_badan) - 1, 0, -1):
        koor_x_baru = semua_part_badan[part_ke - 1].xcor()
        koor_y_baru = semua_part_badan[part_ke - 1].ycor()
        semua_part_badan[part_ke].goto(koor_x_baru, koor_y_baru)
    semua_part_badan[0].forward(20)



screen.exitonclick()