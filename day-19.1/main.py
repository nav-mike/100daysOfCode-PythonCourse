from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color.")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = {}
is_race_on = False

for index in range(len(colors)):
    tim = Turtle(shape="turtle")
    tim.color(colors[index])
    tim.penup()
    tim.goto(x=-230, y=index * 60 - 145)
    turtles[colors[index]] = tim

if user_bet:
    is_race_on = True

while is_race_on:
    for color in colors:
        if turtles[color].xcor() >= 230:
            if user_bet == color:
                print("You are the winner!")
            else:
                print(f"Oh no! You are the looser. {color} is the winner")
            is_race_on = False
            break

        turtles[color].forward(random.randint(0, 10))

screen.exitonclick()
