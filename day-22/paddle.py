from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x):
        super().__init__(shape="square")
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setpos(x=x, y=0)

    def up(self):
        if self.ycor() >= 240:
            return

        self.sety(self.ycor() + 20)

    def down(self):
        if self.ycor() <= -240:
            return

        self.sety(self.ycor() - 20)


class LeftPaddle(Paddle):
    def __init__(self):
        super().__init__(x=-350)


class RightPaddle(Paddle):
    def __init__(self):
        super().__init__(x=350)
