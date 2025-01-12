import turtle as t
import random
# import colorgram

# colors = colorgram.extract('day018_hirstpainting/hirst-painting.jpg', 15)

# list_rgb = []
# for i in range(len(colors)):
#     list_rgb.append((colors[i].rgb[0], colors[i].rgb[1], colors[i].rgb[2]))

# print(list_rgb)

# list colors ini dapatnya dari colorgram di atas yang di komen
colors = [(235, 234, 231), (229, 223, 225), (194, 159, 126), (18, 103, 149), (144, 75, 93), (233, 237, 234), (134, 93, 77), (129, 157, 176), (221, 227, 233), (193, 150, 159), (4, 65, 99), (207, 180, 187), (148, 167, 163), (189, 93, 76), (217, 193, 154)]

tim = t.Turtle()
t.colormode(255)


for baris in range(1, 11):
    for _ in range(10):
        tim.dot(20, random.choice(colors))
        tim.penup()
        tim.forward(50)
    # idenya balikin lagi ke origin pakai home(), 
    # terus gerakin ke atas dan belokin ke kanan, 
    # lalu jalanin loop di atas lagi
    tim.home()
    tim.setheading(90)
    tim.forward(baris*50)
    tim.setheading(0)


screen = t.Screen()
screen.exitonclick()


# skip angela dulu, 
# karena caranya kelihatan kurang efektif
