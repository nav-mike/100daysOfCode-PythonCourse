from turtle import Turtle


class Snake:
    MOVE_DISTANCE = 20

    LEFT = 180
    RIGHT = 0
    UP = 90
    DOWN = 270

    def __init__(self, length=3):
        self.snake = []
        for i in range(length):
            t = Turtle(shape="square")
            t.color("white")
            t.penup()
            t.goto(i * -20, 0)
            self.snake.append(t)
        self.head = self.snake[0]

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            x, y = self.snake[i - 1].pos()
            self.snake[i].goto(x, y)

        self.head.forward(self.MOVE_DISTANCE)

    def eat(self):
        t = Turtle(shape="square")
        t.color("white")
        t.penup()
        t.goto(self.snake[-1].pos())
        self.snake.append(t)

    def size(self):
        return len(self.snake) - 3

    def left(self):
        if self.head_is_not(self.RIGHT):
            self.head.setheading(self.LEFT)

    def right(self):
        if self.head_is_not(self.LEFT):
            self.head.setheading(self.RIGHT)

    def up(self):
        if self.head_is_not(self.DOWN):
            self.head.setheading(self.UP)

    def down(self):
        if self.head_is_not(self.UP):
            self.snake[0].setheading(self.DOWN)

    def head_is_not(self, direction):
        return self.head.heading() != direction

    def is_inside_snake(self, x, y):
        for t in self.snake[1:]:
            if t.distance(x, y) < 10:
                return True
        return False

    def reset_snake(self):
        for t in self.snake:
            t.goto(1000, 1000)
        self.snake.clear()
        for i in range(3):
            t = Turtle(shape="square")
            t.color("white")
            t.penup()
            t.goto(i * -20, 0)
            self.snake.append(t)
        self.head = self.snake[0]
