from random import randint, choice
from turtle import Turtle

""" colors of cars """
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

""" starting distance is steps of turtle """
STARTING_MOVE_DISTANCE = 5
""" MOVE_INCREMENT is amount of increment car steps in any level up"""
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []

    def car_creator(self):
        """
        create a object in car class with random color
        """
        new_car = Turtle()
        chance = randint(1, 5)
        if chance == 1:
            new_car.penup()
            new_car.shape('square')
            new_car.shapesize(0.5, 1.5, 1)
            new_car.color(choice(COLORS))
            new_car.goto(400, randint(-240, 240))
            self.all_cars.append(new_car)

    def move_the_car(self, level):
        """
        move the car depend on the level
        """
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE + (MOVE_INCREMENT*level))
