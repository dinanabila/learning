from turtle import Turtle

class Pemain(Turtle):

    def __init__(self, koor_awal = ()):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(x=koor_awal[0], y=koor_awal[1])


    def ke_atas(self):
        koor_y = self.ycor() + 30
        self.goto(x=self.xcor(), y=koor_y)

    def ke_bawah(self):
        koor_y = self.ycor() - 30
        self.goto(x=self.xcor(), y=koor_y)
