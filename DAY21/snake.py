from turtle import Turtle
from sound import eating_sound

POSITION = [(0, 0), (-20, 0), (-40, 0)]  # positions of beginning
STEPS = 20


class Snake:
    def __init__(self):
        self.snake_body = []
        self.snake_creator()
        self.head = self.snake_body[0]

    # create snake body with three turtle
    def snake_creator(self):
        for place in POSITION:
            part = Turtle("square")
            part.color("white")
            part.speed("fastest")
            part.penup()
            part.goto(place)
            self.snake_body.append(part)

    # a function for move our snake automatically
    def move(self):
        for snake in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[snake - 1].xcor()
            new_y = self.snake_body[snake - 1].ycor()
            self.snake_body[snake].goto(new_x, new_y)
        self.head.forward(20)

    # increase length of body when snake eat the food
    def increase_length(self):
        """
        this is a function for increase length of snake body
        :return:
        """
        x = self.snake_body[-1].xcor()
        y = self.snake_body[-1].ycor()
        self.move()
        new_part = Turtle("square")
        new_part.penup()
        new_part.color("white")
        new_part.speed("fast")
        new_part.goto(x=x, y=y)
        self.snake_body.append(new_part)

    # functions for control our snake by keyboard
    # "if" statements are for forbidding moving revers
    def up(self):
        if self.head.heading() == 270:
            return 0
        else:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() == 90:
            return 0
        else:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() == 0:
            return 0
        else:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() == 180:
            return 0
        else:
            self.head.setheading(0)



