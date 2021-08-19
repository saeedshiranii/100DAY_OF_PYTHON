from turtle import Turtle


def line():
    """
    this function draw two line in the screen
    """
    for y in (-260, 260):
        liner = Turtle()
        liner.color("white")
        liner.hideturtle()
        liner.penup()
        liner.goto(-700, y)
        liner.pendown()
        liner.forward(1400)
