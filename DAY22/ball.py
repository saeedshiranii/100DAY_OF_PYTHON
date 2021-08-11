from turtle import Turtle
from random import randint, choice
MOVE_STEPS = [10, 20, 30, -10, -20, -30]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.y_step = 10
        self.x_step = 10

    def move(self):
        new_x = self.xcor() + self.x_step
        new_y = self.ycor() + self.y_step
        self.goto(new_x, new_y)

    def revers(self):
        self.y_step *= -1



































