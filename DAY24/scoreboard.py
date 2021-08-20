from turtle import Turtle
""" position and font of scoreboard """
Movement = False
ALIGN = "center"
TUPLE = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt', mode="r") as file:
            high_score = file.read()
        self.high_score = high_score
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=270)

    def update_scoreboard(self):
        """
        create and update your scoreboard
        :return:
        """
        self.write(arg=F"Score : {self.score}   HIGH_SCORE : {self.high_score}", move=Movement, align=ALIGN, font=TUPLE)

    def game_over(self):
        """
        when snake touch walls or touch a part of his body game is over
        this function create turtle in center of screen and write: GAME OVER
        :return:
        """
        self.goto(0, 0)
        self.write(arg=F"GAME OVER", move=Movement, align=ALIGN, font=TUPLE)

    def clear_data(self):
        self.clear()

    def increase_score(self):
        """
        each time snake eat a food you will get a score
        this function should clear your previous score and put a new one
        :return:
        """
        self.write(arg=F"Score : {self.score}   HIGH_SCORE : {self.high_score}", move=Movement, align=ALIGN, font=TUPLE)
        self.clear()
        self.score += 1
        if self.score > int(self.high_score):
            with open('data.txt', mode="w") as file:
                file.write(str(self.score))
        self.write(arg=F"Score : {self.score}   HIGH_SCORE : {self.high_score}", move=Movement, align=ALIGN, font=TUPLE)

