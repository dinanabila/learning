from turtle import Turtle

# tambahan angela: jadiin constant biar gampang dimodif kalau bosen
POSISI_AWAL = [(0, 0), (-20, 0), (-40, 0)]
BESAR_LANGKAH = 20
ATAS = 90
BAWAH = 270
KIRI = 180
KANAN = 0

class Snake():

    def __init__(self):
        self.semua_part_badan = []

        # tambahan dari angela
        self.bikin_snake()
        self.kepala = self.semua_part_badan[0]

    def bikin_snake(self):
        for posisi in POSISI_AWAL:
            part_badan = Turtle("square")
            part_badan.color("white")
            part_badan.penup()
            part_badan.goto(posisi)
            self.semua_part_badan.append(part_badan)

    def move(self):
        for part_ke in range(len(self.semua_part_badan) - 1, 0, -1):
            koor_x_baru = self.semua_part_badan[part_ke - 1].xcor()
            koor_y_baru = self.semua_part_badan[part_ke - 1].ycor()
            self.semua_part_badan[part_ke].goto(koor_x_baru, koor_y_baru)
        self.kepala.forward(BESAR_LANGKAH)

    
    def ke_atas(self):
        if self.kepala.heading() != BAWAH:
            self.kepala.setheading(ATAS)

    def ke_bawah(self):
        if self.kepala.heading() != ATAS:
            self.kepala.setheading(BAWAH)

    def ke_kanan(self):
        if self.kepala.heading() != KIRI:
            self.kepala.setheading(KANAN)

    def ke_kiri(self):
        if self.kepala.heading() != KANAN:
            self.kepala.setheading(KIRI)