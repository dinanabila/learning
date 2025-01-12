from turtle import Turtle, Screen

tim = Turtle()
colors = ["khaki", "indianred", "OliveDrab", "Navy", "orchid", "linen", "tan", "red", "bisque", "blue"]

for i in range(3,11):
    for _ in range(i):
        # ubah warna pen
        tim.pencolor(colors[i-3])
        # maju
        tim.forward(100)
        # ubah ke arah kanan sebesar sekian derajat
        tim.right(360/i)

screen = Screen()
screen.exitonclick()