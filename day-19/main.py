from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


screen.listen()


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.onkey(key="Up", fun=lambda: tim.forward(10))
screen.onkey(key="Down", fun=lambda: tim.backward(10))
screen.onkey(key="a", fun=lambda: tim.left(10))
screen.onkey(key="d", fun=lambda: tim.right(10))
screen.onkey(key="c", fun=clear)

screen.exitonclick()
