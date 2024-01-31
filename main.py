from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Cross The Road Challenge")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True


while game_is_on:
    time.sleep(scoreboard.speed)
    screen.update()
    car_manager.generate_car()
    car_manager.move()
    for car in car_manager.new_cars:
        if player.distance(car) < 22:
            player.goto(0, -280)
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() >= 270:
        scoreboard.update_score()
        player.restart()
screen.exitonclick()
