import turtle as t
import random

colors = ["khaki", "indianred", "OliveDrab", "Navy", "orchid", "linen", "tan", "orchid", "bisque", "sienna"]

tim = t.Turtle()
tim.width(10)

# def maju():
#     tim.forward(40)

def belok_kanan():
    tim.right(90)
    tim.forward(40)

def belok_kiri():
    tim.left(90)
    tim.forward(40)

daftar_gerakan = [belok_kanan, belok_kiri]

# for _ in range(10):
while True:
    warna = random.choice(colors)
    tim.pencolor(warna)
    gerakan = random.choice(daftar_gerakan)
    gerakan()


    screen = t.Screen()
