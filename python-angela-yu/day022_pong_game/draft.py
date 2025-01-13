from turtle import Screen, Turtle
from paddle import Pemain
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0) 

# ============
# BIKIN PLAYER
# ============

# pemain = Turtle("square")
# pemain.shapesize(stretch_wid=5, stretch_len=1)
# pemain.color("white")
# pemain.penup()
# pemain.goto(x=350, y=0)


# def ke_atas():
#     koor_y = pemain.ycor() + 30
#     pemain.goto(x=pemain.xcor(), y=koor_y)

# def ke_bawah():
#     koor_y = pemain.ycor() - 30
#     pemain.goto(x=pemain.xcor(), y=koor_y)

pemain_kanan = Pemain((350,0))
pemain_kiri = Pemain((-350,0))

bola = Ball()
skor = Scoreboard()

# ==========
# BIKIN BOLA
# ==========

# bola = Turtle()
# bola.shape("circle")
# bola.color("white")
# bola.width(5)
# bola.penup()


screen.listen()
screen.onkey(fun=pemain_kanan.ke_atas, key="Up")
screen.onkey(fun=pemain_kanan.ke_bawah, key="Down")
screen.onkey(fun=pemain_kiri.ke_atas, key="w")
screen.onkey(fun=pemain_kiri.ke_bawah, key="s")



masih_main = True
while masih_main:
    time.sleep(0.07)
    screen.update()
    bola.move()
    
    # =================================
    # NABRAK DINDING ATAS BAWAH? MANTUL
    # =================================

    if bola.ycor() > 280 or bola.ycor() < -280:
        # mantul
        bola.mantul_y()
        bola.nambah_cepet()


    # =====================
    # NABRAK PEMAIN? MANTUL
    # =====================

    if bola.distance(pemain_kanan) < 50 and bola.xcor() > 320 or bola.distance(pemain_kiri) < 50 and bola.xcor() < -320:
        bola.mantul_x()


    # ==============================================================================
    # GAGAL NANGKEP BOLA? BALIKIN BOLA KE TENGAH, TERUS GERAKIN KE ARAH PEMAIN LAWAN
    # ==============================================================================

    if bola.xcor() > 380: 
        bola.balik_ke_tengah()
        skor.tambah_skor_pemain_kiri()


    if bola.xcor() < -380:
        bola.balik_ke_tengah()
        skor.tambah_skor_pemain_kanan()

screen.exitonclick()