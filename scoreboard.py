from turtle import Turtle

NORMAL = font = ("Arial", 24, "normal")

CENTER = "center"


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)

        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"score: {self.score} High score: {self.high_score}", align=CENTER, font=NORMAL)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()
