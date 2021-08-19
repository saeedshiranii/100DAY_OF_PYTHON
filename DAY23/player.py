from turtle import Turtle

""" starting position of turtle player """
STARTING_POSITION = (0, -280)
""" MOVE_DISTANCE is length of steps of turtle """
MOVE_DISTANCE = 10
""" FINISH_LINE_Y is the line which turtle crossed it game is will be level up """
FINISH_LINE_Y = 300


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.shapesize(0.8, 0.8, 1)
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def reset_player(self):
        """
        set begin potion for turtle in new level
        """
        if self.ycor() > 250:
            self.goto(0, -280)

    def move_up(self):
        """
        move the turtle up by MOVE_DISTANCE steps
        """
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        """
        move the turtle down by MOVE_DISTANCE steps
        """
        self.setheading(270)
        self.forward(MOVE_DISTANCE)

