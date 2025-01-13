from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(310, random.randint(-200, 200))
        self.kecepatan = STARTING_MOVE_DISTANCE

    def move(self):
        x_baru = self.xcor() - self.kecepatan
        self.goto(x_baru, self.ycor())

    def tambah_ngebut(self):
        self.kecepatan += MOVE_INCREMENT

