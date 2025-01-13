from turtle import Turtle

# tambahan angela: jadiin constant
ALIGNMENT = "center"
FONT = ("Arial", 20, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.skor = 0
        self.hideturtle()
        self.pencolor("white")
        self.akumulasi_skor()


    def akumulasi_skor(self):
        # kalau berhasil nabrak makanan, tambah skor
        # ini udah ada di main.py, kondisinya
        # jadi di sini tinggal tambahin skor aja
        self.clear()
        self.penup()
        self.goto(0, 250)
        self.skor += 1
        self.write(f"Score: {self.skor}", align=ALIGNMENT, font=FONT)

    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        

