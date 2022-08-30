from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, level=1):
        super().__init__(shape="square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.reset_position()
        self.car_speed = STARTING_MOVE_DISTANCE + ((level - 1) * MOVE_INCREMENT)

    def move(self):
        self.setx(self.xcor() - self.car_speed)

    def reset_position(self):
        self.setposition(x=280, y=random.randint(-250, 250))
        self.color(COLORS[random.randint(0, len(COLORS) - 1)])

    def update_speed(self):
        self.car_speed += MOVE_INCREMENT

