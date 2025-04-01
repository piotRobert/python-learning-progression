from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score_point = 0
        with open("d20_21_snake_game/data.txt") as data:
            self.high_score = int(data.read())
        self.shape(None)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score_point} High score: {self.high_score}", align=ALIGNMENT, font = FONT)

    def increase_score(self):
        self.score_point += 1
        self.update_scoreboard()
    
    def reset(self):
        if self.score_point > self.high_score:
            self.high_score = self.score_point
            with open("d20_21_snake_game/data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score_point = 0 
        self.update_scoreboard()