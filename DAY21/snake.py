from turtle import Turtle

POSITION = [(0, 0), (-20, 0), (-40, 0)]
STEPS = 20


class Snake:
    def __init__(self):
        self.snake_body = []
        self.snake_creator()
        self.head = self.snake_body[0]

    def snake_creator(self):
        for place in POSITION:
            part = Turtle("square")
            part.color("white")
            part.penup()
            part.goto(place)
            self.snake_body.append(part)

    def move(self):
        for snake in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[snake - 1].xcor()
            new_y = self.snake_body[snake - 1].ycor()
            self.snake_body[snake].goto(new_x, new_y)
        self.head.forward(20)

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



