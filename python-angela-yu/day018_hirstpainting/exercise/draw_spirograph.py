import turtle as t
import random

tim = t.Turtle()
tim.speed("fastest")
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)


def gambar_spirograph(panjang_celah):
    # tadinya aku gini, tanpa fungsi juga
    # for i in range(20):
    for _ in range(int(360 / panjang_celah)):
        tim.pencolor(random_color())
        # tadinya aku gini:
        # tim.setheading(i*18)
        tim.setheading(tim.heading() + panjang_celah)
        tim.circle(100)

gambar_spirograph(5)

screen = t.Screen()
screen.exitonclick()