from turtle import Turtle
from random import randint

colors = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager:

    def __init__(self):
        self.new_cars = []


    def move(self):
        for car in self.new_cars:
            car.backward(5)

    def generate_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(colors[randint(a=0, b=len(colors) - 1)])
            random_y_position = randint(-245, 260)
            new_car.goto(300, random_y_position)
            self.new_cars.append(new_car)

