from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

ular = Snake()
makanan = Food()
skor = Scoreboard()

screen.listen()
screen.onkey(fun = ular.ke_atas, key = "Up")
screen.onkey(fun = ular.ke_bawah, key = "Down")
screen.onkey(fun = ular.ke_kanan, key = "Right")
screen.onkey(fun = ular.ke_kiri, key = "Left")

masih_hidup = True
while masih_hidup:
    screen.update()
    time.sleep(0.1)
    ular.move()

    # Nabrak makanan?
    if ular.kepala.distance(makanan) < 15:
        makanan.refresh()
        skor.akumulasi_skor()
        ular.memanjang()

    # Nabrak dinding?
    if ular.kepala.xcor() > 280 or ular.kepala.xcor() < -280 or ular.kepala.ycor() > 280 or ular.kepala.ycor() < -280:
        skor.reset()
        ular.reset()

    # Nabrak badan?
    # if kepala nabrak part badan:
        # trigger game_over
    for part in ular.semua_part_badan[1:]:
        # if part == ular.kepala:
        #     pass
        # elif ular.kepala.distance(part) < 10:
        if ular.kepala.distance(part) < 10:
            skor.reset()
            ular.reset()
        



screen.exitonclick()