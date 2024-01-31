from turtle import Turtle

FONT = ('arial', 12, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-270, 270)
        self.level = 1
        self.speed = 0.1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level=  {self.level}", align='left', font=FONT)
        self.level += 1
        self.speed *= 0.4

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align='center', font=FONT)

