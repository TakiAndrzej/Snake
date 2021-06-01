from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.setposition(0, 260)
        self.score = 0
        with open("high_score.txt") as file:
            self.high_score= int(file.read())
        self.color("white")
        self.hideturtle()
        self.write_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("high_score.txt", 'w') as file:
            file.write(str(self.high_score))

        self.score = 0
        self.clear()
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
