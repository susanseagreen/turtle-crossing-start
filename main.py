import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crosser")

player = Player()

screen.listen()
screen.onkey(player.go_up, "w")
screen.onkey(player.go_up, "Up")

cars = CarManager()

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move()

    # detect collision with car
    for car in cars.all_cars:
        if car.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()

    # detect a successful crossing
    if player.survived_crossing_road():
        player.go_to_start()
        scoreboard.increase_level()
        cars.speed_up()

screen.exitonclick()
