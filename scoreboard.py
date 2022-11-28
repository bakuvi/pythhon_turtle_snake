from turtle import Turtle

NORMAL = font = ("Arial", 24, "normal")

CENTER = "center"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)

        self.update_score()

    def update_score(self):
        self.write(f"score: {self.score}", align=CENTER, font=NORMAL)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=CENTER, font=NORMAL)
