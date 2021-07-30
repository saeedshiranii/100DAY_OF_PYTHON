import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(600, 500)
bet = screen.textinput(title="Make your bet.", prompt="which turtle will win the race? enter the color.")

tim = Turtle()
tim.hideturtle()
tim.penup()
tim.goto(285, -175)
tim.pendown()
tim.left(90)
tim.forward(350)


start_position = [-75, -45, -15, 15, 45, 75]
turtle_color = ["red",  "orange", "yellow", "purple", "green", "blue"]
all_turtles = []
for index in range(6):
    cute_turtle = Turtle("turtle")
    cute_turtle.penup()
    cute_turtle.color(turtle_color[index])
    cute_turtle.goto(-290, start_position[index])
    all_turtles.append(cute_turtle)


if bet:
    game_on = True
    while game_on:
        for turtle in all_turtles:
            if turtle.xcor() >= 285:
                game_on = False
                winner = turtle.pencolor()
                if bet == winner:
                    print(F"you win. winner is {winner}.")
                    break
                else:
                    print(F"you lose.winner was {winner}.")
            else:
                turtle.forward(random.randint(0, 30))

