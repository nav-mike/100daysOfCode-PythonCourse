import time
from turtle import Screen

from food import Food
from scoreboard import ScoreBoard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        snake.eat()
        food.refresh()
        scoreboard.update(snake.size())

    # Detect collision with border
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or \
            snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset_score()
        snake.reset_snake()

    # Detect collision with itself
    if snake.is_inside_snake(snake.head.xcor(), snake.head.ycor()):
        scoreboard.reset_score()
        snake.reset_snake()

screen.exitonclick()
