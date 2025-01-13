from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.skor_pemain_kanan = 0
        self.skor_pemain_kiri = 0
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.skor_pemain_kiri, align="center", font=("Courier", 70, "normal"))
        self.goto(100, 200)
        self.write(self.skor_pemain_kanan, align="center", font=("Courier", 70, "normal"))

    
    def tambah_skor_pemain_kanan(self):
        self.skor_pemain_kanan += 1
        self.update_scoreboard()

    
    def tambah_skor_pemain_kiri(self):
        self.skor_pemain_kiri += 1
        self.update_scoreboard()

    