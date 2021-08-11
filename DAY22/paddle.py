from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, main_tuple):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.goto(main_tuple)
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")

    def up(self):

        new_y = self.ycor() + 30
        self.sety(new_y)

    def down(self):
        new_y = self.ycor() - 30
        self.sety(new_y)





