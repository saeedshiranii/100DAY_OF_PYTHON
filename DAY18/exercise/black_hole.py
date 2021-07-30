from turtle import Turtle, Screen
import turtle
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


turtle.colormode(255)

black = Turtle()
hole = Turtle()


screen = Screen()

black.speed("fastest")
hole.speed("fastest")


#hole.setx(150)
for i in range(100):

    black.forward(180)
    hole.forward(180)
    black.color(random_color())
    hole.color(random_color())
    black.left(70)
    hole.left(70)
    black.forward(60)
    hole.forward(60)
    black.right(40)
    hole.right(40)

    black.penup()
    hole.penup()
    black.setposition(0, 0)
    hole.setposition(100, 0)
    black.pendown()
    hole.pendown()

    black.right(2)
    hole.right(2)

turtle.done()

screen.exitonclick()
