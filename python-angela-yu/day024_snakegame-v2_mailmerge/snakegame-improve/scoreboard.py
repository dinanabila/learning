from turtle import Turtle

# tambahan angela: jadiin constant
ALIGNMENT = "center"
FONT = ("Arial", 20, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.skor = -1
        with open('day024_snakegame-v2/snakegame-improve/data.txt') as file:
            self.highscore = int(file.read())
        self.hideturtle()
        self.pencolor("white")
        self.akumulasi_skor()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.skor}  Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)


    def akumulasi_skor(self):
        # kalau berhasil nabrak makanan, tambah skor
        # ini udah ada di main.py, kondisinya
        # jadi di sini tinggal tambahin skor aja
        self.clear()
        self.penup()
        self.goto(0, 250)
        self.skor += 1
        self.update_scoreboard()

    def reset(self):
        if self.skor > self.highscore:
            with open('day024_snakegame-v2/snakegame-improve/data.txt', mode="w") as file:
                self.highscore = file.write(str(self.skor))

        self.skor = 0
        self.update_scoreboard()


    # versi sebelumnya
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        

