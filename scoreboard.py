from turtle import Turtle
from car_manager import Car
FONT = ("Courier", 10, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-200, 270)
        self.score = 0
        self.level = 1

    def update_scorecard(self):
        self.update_level()
        self.update_score()
        self.write(f"Score : {self.score} Level : {self.level}", align="center", font=FONT)

    def update_score(self):
        self.clear()
        self.score += 5

    def update_level(self):
        self.clear()
        self.level += 1

