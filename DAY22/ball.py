from turtle import Turtle


class Ball(Turtle):
    """
    this class is for create a ball in center of screen
    """
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_step = 10
        self.x_step = 10

    def move(self):
        """
        this function move the ball on a straight line
        :return:
        """
        new_x = self.xcor() + self.x_step
        new_y = self.ycor() + self.y_step
        self.goto(new_x, new_y)

    def y_revers(self):
        """
         you can use this function
        for make revers direction in y
        :return:
        """
        self.y_step *= -1

    def x_revers(self):
        """
        you can use this function
        for make revers direction in x
        :return:
        """
        self.x_step *= -1
