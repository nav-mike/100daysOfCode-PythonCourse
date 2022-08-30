import random
import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

timmy = Player()
screen.onkey(timmy.move, "Up")

cars = [CarManager()]

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    for car in cars:
        car.move()

        if car.xcor() < -1 * FINISH_LINE_Y:
            car.reset_position()

    if len(cars) < 20 and cars[-1].xcor() < 250 and random.randint(1, 5) == 1:
        cars.append(CarManager(scoreboard.level))

    if timmy.ycor() > FINISH_LINE_Y:
        timmy.reset_position()
        scoreboard.level_up()
        for car in cars:
            car.update_speed()

    for car in cars:
        if timmy.distance(car) < 20:
            game_is_on = False
            break

screen.exitonclick()
