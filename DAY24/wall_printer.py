from turtle import Turtle

# create a line along the screen for better user experience


def wall_printer(turtle_color):
    """
    these several line are gonna create four beautiful walls
    i write this without loop because positions was not certain (because of scoreboard)
    :param turtle_color:
    :return:
    """
    border = Turtle()
    border.hideturtle()
    border.speed("fastest")
    border.penup()
    border.pencolor(turtle_color)
    border.goto(-390, -290)
    border.pendown()
    border.forward(780)
    border.setheading(90)
    border.forward(560)
    border.setheading(180)
    border.forward(780)
    border.setheading(270)
    border.forward(560)
