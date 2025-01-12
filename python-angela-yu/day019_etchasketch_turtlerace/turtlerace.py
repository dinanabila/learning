from turtle import Turtle, Screen
from random import randint

screen = Screen()

# atur luas screen gui nya
screen.setup(width=500, height=400)

# bikin pop up window buat nanya user
tebakan_user = screen.textinput(title="Tebak siapa yang menang", prompt="Coba tebak, kura-kura warna apa yang bakal menang? (ketik red/yellow/green/blue/purple): ")
colors = ["red", "yellow", "green", "blue", "purple"]
koor_y = [-80, -40, 0, 40, 80]

# ==========================================
# ALAMAK KIRAIN HARUS BEDA NAMA KURA-KURANYA
# ==========================================

# tom = Turtle(shape="turtle")
# tom.color(colors[1])
# tom.penup()
# tom.goto(x=-220, y=-40)

# jim = Turtle(shape="turtle")
# jim.color(colors[2])
# jim.penup()
# jim.goto(x=-220, y=-80)

# pam = Turtle(shape="turtle")
# pam.color(colors[3])
# pam.penup()
# pam.goto(x=-220, y=40)

# zul = Turtle(shape="turtle")
# zul.color(colors[4])
# zul.penup()
# zul.goto(x=-220, y=80)

# ==========
# ALAMAK END
# ==========

# harusnya gini aja kalau angela
semua_turtle = []

for turtle_ke in range(0,5):
    turtle_baru = Turtle(shape="turtle")
    turtle_baru.color(colors[turtle_ke])
    turtle_baru.penup()
    turtle_baru.goto(x=-220, y=koor_y[turtle_ke])
    semua_turtle.append(turtle_baru)

# bikin kura-kuranya balapan
if tebakan_user:
    balapan = True

while balapan:

    for turtle in semua_turtle:
        if turtle.xcor() > 230:
            balapan = False
            warna_pemenang = turtle.pencolor()
            if warna_pemenang == tebakan_user:
                print(f"Tebakanmu benar! Kura-kura {warna_pemenang} yang menang 'v')b")
            else:
                print(f"Ah, ternyata bukan {tebakan_user} yang menang. Pemenangnya kura-kura {warna_pemenang} DDD:")
        jarak_acak = randint(0, 10)
        turtle.forward(jarak_acak)
    

screen.exitonclick()