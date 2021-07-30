import random
from turtle import Screen
import turtle as t

t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


tim = t.Turtle()
tim.speed("fastest")
for i in range(500):
    tim.color(random_color())
    tim.circle(150)
    tim.left(1)
    print(i)

screen = Screen()
screen.exitonclick()
