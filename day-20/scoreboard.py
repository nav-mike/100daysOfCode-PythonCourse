import os
from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.high_score = 0
        self.score = 0
        self.hideturtle()
        self.goto(x=0, y=285)
        self.color("white")
        if os.path.exists("high_score.txt"):
            with open("high_score.txt", "r") as f:
                self.high_score = int(f.read())
        self.update_score()

    def update(self, score):
        self.score = score
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier", 12, "normal"))

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as f:
                f.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write(f"GAME OVER.", align="center",
    #                font=("Courier", 24, "normal"))
