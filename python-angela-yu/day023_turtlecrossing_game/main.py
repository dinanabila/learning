import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

pemain = Player()
semua_mobil = []
penghitung = 0
level = Scoreboard()

screen.listen()
screen.onkey(pemain.maju, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # increment hitungan mobil lewat
    penghitung += 1

    if penghitung % 8 == 0:
        mobil_baru = CarManager()
        semua_mobil.append(mobil_baru)
    
    # masukin mobil yang udah digenerate ke list,
    # biar masing-masing mobilnya bisa dikasih perintah move()
    for mobil in semua_mobil:
        mobil.move()

    # nabrak dinding paling atas (player berhasil nyampe garis finish?)
    if pemain.ycor() > 280:
        for mobil in semua_mobil:
            mobil.hideturtle()
        pemain.balik_ke_awal()
        semua_mobil = []
        mobil.tambah_ngebut()
        level.update_level()

    # kura-kura ketabrak mobil
    for mobil in semua_mobil:
        if mobil.distance(pemain) < 20:
            level.game_over()
            game_is_on = False



screen.exitonclick()

    

