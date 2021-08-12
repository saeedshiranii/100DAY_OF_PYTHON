from turtle import Turtle


def line():
    """
    draw a line in screen
    :return:
    """
    turtle = Turtle()
    turtle.penup()
    turtle.goto(0, 300)
    turtle.setheading(270)
    turtle.pencolor("white")
    turtle.pensize(12)
    turtle.pendown()

    while turtle.ycor() > -300:
        turtle.forward(30)
        turtle.penup()
        turtle.forward(20)
        turtle.pendown()
