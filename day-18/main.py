import turtle
import random

import colorgram
from turtle import Turtle, Screen

rgb_colors = list(map(lambda color: (color.rgb.r, color.rgb.g, color.rgb.b), colorgram.extract('image.jpg', 30)))

tim = Turtle()
turtle.colormode(255)
tim.penup()
tim.hideturtle()

for i in range(-5, 5):
    for j in range(-5, 5):
        tim.setpos(j * 50, i * 50)
        tim.dot(20, random.choice(rgb_colors))

screen = Screen()
screen.exitonclick()
