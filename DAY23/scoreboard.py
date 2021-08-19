from turtle import Turtle

""" font of game over """
GAME_OVER_FONT = ("Verdana", 60, "normal")

""" font of scoreboard """
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """
    this class create two model object
    1.scoreboard
    2."game over" alarm
    """
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()

    def scoreboard(self, score):
        self.clear()
        self.goto(-250, 260)
        self.write(arg=F"score: {score}", move=False, align="center", font=FONT)

    def game_over(self):
        self.color("red")
        self.write(arg="GAME OVER", move=False, align="center", font=GAME_OVER_FONT)



