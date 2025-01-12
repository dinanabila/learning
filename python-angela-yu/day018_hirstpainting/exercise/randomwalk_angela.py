import turtle as t
import random

# colors = ["khaki", "indianred", "OliveDrab", "Navy", "orchid", "linen", "tan", "orchid", "bisque", "sienna"]
arah = [0, 90, 180, 270]


tim = t.Turtle()
tim.width(10)
tim.speed("fastest")
t.colormode(255)


# bikin generator warna acak
# kenapa dalam bentuk tuple, soalnya modul turtle butuhnya color dalam bentuk rgb tuple
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)



for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(arah))