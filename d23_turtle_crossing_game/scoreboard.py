from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-220,260)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def update_score(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def gameover(self):
        self.goto(0,0)
        self.write(f"Game over", align="center", font=FONT)