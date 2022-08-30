# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.color("coral")
# timmy.shape("turtle")
# timmy.forward(100)
#
# my_screen = Screen()
# my_screen.bgcolor("lightblue")
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column('Pokemon Name', ['Pikachu', 'Charmander', 'Squirtle'], align='l')
table.add_column('Type', ['⚡️', '🔥', '💧'])

print(table)

