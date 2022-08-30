import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

screen.addshape("./blank_states_img.gif")
turtle.shape("./blank_states_img.gif")

data = pandas.read_csv("./50_states.csv")

is_playing = True

while is_playing:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")

    if not answer_state:
        is_playing = False
        break

    answer_state = answer_state.strip().title()
    state = data[data.state == answer_state]
    if not state.empty:
        s = turtle.Turtle()
        s.penup()
        s.hideturtle()
        s.setposition(x=int(state.x), y=int(state.y))
        s.write(answer_state)
