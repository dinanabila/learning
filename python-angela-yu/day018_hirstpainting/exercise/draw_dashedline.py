from turtle import Turtle, Screen

tim = Turtle()

for _ in range(5):
    tim.forward(10)
    # penup() itu untuk nahan pena ke atas biar pas gerak, ga norehin tinta
    tim.penup()
    tim.forward(10)
    # pendown() itu untuk balikin pena ke kertas, biar pas turtlenya gerak bisa kegores tintanya
    tim.pendown()
    # tim.forward(10)
    # tim.penup()
    # tim.forward(10)
    # tim.pendown()
    # tim.forward(10)

screen = Screen()
screen.exitonclick()