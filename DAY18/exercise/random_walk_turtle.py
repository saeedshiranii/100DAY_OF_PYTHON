from turtle import Turtle, Screen
import turtle
import random


y = Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


angle = [90, 180, 270, 360]


def walk():
    y.hideturtle()
    y.pensize(20)
    y.speed("fastest")
    for _ in range(500):
        y.pencolor(random_color())
        y.setheading(random.choice(angle))
        y.forward(75)

    screen = Screen()
    screen.exitonclick()


walk()
