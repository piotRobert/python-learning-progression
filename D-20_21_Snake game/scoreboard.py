from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape(None)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.score_point = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score_point}", align=ALIGNMENT, font = FONT)
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font = FONT)
    
    def refresh_score(self):
        self.score_point += 1
        self.clear()
        self.update_scoreboard()