from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.update_level()

    
    def update_level(self):
        self.clear()
        self.goto(-280, 250)
        self.level += 1
        self.write(f"Level: {self.level}", align="left", font=FONT)
    
    
    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=FONT)
