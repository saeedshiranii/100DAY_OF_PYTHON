from turtle import Turtle, Screen

screen = Screen()
tim = Turtle()
screen.listen()


def forward():
    tim.forward(10)


def backward():
    tim.backward(10)


def counter_clockwise():
    tim.left(10)


def clockwise():
    tim.right(10)



def clear_screen():
    screen.resetscreen()


screen.onkey(forward, "W")
screen.onkey(backward, "S")
screen.onkey(counter_clockwise, "A")
screen.onkey(clockwise, "D")
screen.onkey(clear_screen, "C")


screen.exitonclick()
