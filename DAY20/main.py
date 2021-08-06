import time
from turtle import Turtle, Screen

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("my snake")


x = 0
snake_body = []
for _ in range(3):

    tim = Turtle("square")
    tim.color("white")
    tim.penup()
    tim.setposition(x, 0)
    snake_body.append(tim)
    x += -20

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)



screen.exitonclick()
