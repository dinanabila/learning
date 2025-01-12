from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

ular = Snake()

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



screen.exitonclick()