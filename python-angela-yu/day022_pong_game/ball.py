from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.width(5)
        self.penup()
        self.x_move = 10
        self.y_move = 10 # dibikin gini supaya bisa mantul bolanya (manipulasi *=-1)

    def move(self):
        x_baru = self.xcor() + self.x_move
        y_baru = self.ycor() + self.y_move
        self.goto(x_baru, y_baru)

    def mantul_y(self):
        self.y_move *= -1

    def mantul_x(self):
        self.x_move *= -1

    def balik_ke_tengah(self):
        self.home()
        self.x_move = 10
        self.mantul_x()

    def nambah_cepet(self):
        self.x_move += 5


 