from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed("fastest")

    def refresh(self, random_color):
        """
        create food with random color in random places
        :param random_color:
        :return:
        """
        self.color(random_color)
        self.goto(random.randint(-370, 370), random.randint(-270, 250))



