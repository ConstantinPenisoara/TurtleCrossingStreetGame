from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("Black")
        self.setheading(90)
        self.penup()
        self.goto(0, -280)

    def up(self):
        new_y = self.ycor() + 5
        self.goto(0, new_y)

    def restart(self):
        self.goto(0, -280)
