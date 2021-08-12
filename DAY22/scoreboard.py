from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        """
        create an object for show a number on the screen
        """
        super().__init__()

    def create_scoreboard(self, align, score):
        """
        :param align:
        align is an argument for the place of scoreboard: "left", "right", "center"
        :param score:
        score is a int number for show who win the past turn
        :return:
        """
        self.write(arg=score, move=False, align=align, font=('Arial', 45, "normal"))
