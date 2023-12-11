import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")

screen.listen()
player = Player()
scoreboard = Scoreboard()
screen.onkeypress(player.moveup, "w")
screen.onkeypress(player.movedown, "s")

game_is_on = True
cars = []
while game_is_on:
    time.sleep(scoreboard.difficulty)
    if random.randint(1, 3) == 1:
        car = CarManager()
        cars.append(car)
    for car in cars:
        car.move()
        if player.distance(car) < 20:
            game_is_on = False
    if player.ycor() >= 285:
        player.next_round()
        scoreboard.increase_difficulty()
        scoreboard.update_score()

    screen.update()


screen.exitonclick()
