from turtle import Turtle
ALIGNMENT = "Center"
FONT = ("arial", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.up()
        self.goto(0, 270)
        self.updatescore()
        self.hideturtle()

    def track(self):
        self.score += 1
        self.updatescore()

    def updatescore(self):
        self.clear()
        self.write(f"Your score {self.score} High score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")

        self.score = 0
        self.updatescore()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER\n\nYour final score was: {self.score}", font=("italic", 24, "bold"), align=ALIGNMENT)



