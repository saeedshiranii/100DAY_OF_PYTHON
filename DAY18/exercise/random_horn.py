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
ra = 150
q = 0
for i in range(500):
    j = 0
    q += 0.001
    while j < 5:
        tim.circle(ra)
        tim.color(random_color())
        tim.left(1.5)
        j += 1
    ra -= (0.5 + q)


screen = Screen()
screen.exitonclick()
