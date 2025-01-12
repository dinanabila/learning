from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
heading = 0

def maju():
    tim.forward(10)

def mundur():
    tim.backward(10)

def lawanjarumjam():
    global heading
    heading += 25
    tim.setheading(heading)
    return heading

def arahjarumjam():
    global heading
    heading -= 25
    tim.setheading(heading)
    return heading

def hapussemua():
    tim.clear()

screen.listen()
screen.onkey(fun = maju, key = "w")
screen.onkey(fun = mundur, key = "s")
screen.onkey(fun = lawanjarumjam, key = "a")
screen.onkey(fun = arahjarumjam, key = "d")
screen.onkey(fun = hapussemua, key = "c")
screen.exitonclick()