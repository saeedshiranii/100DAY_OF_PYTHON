from car_manager import CarManager
from scoreboard import Scoreboard
from turtle import Screen, Turtle
from player import Player
from line import line
import time

FINISH_LINE_Y = 300

""" create a screen """
screen = Screen()
screen.bgcolor("black")
screen.setup(width=700, height=600)
screen.tracer(0)
line()

""" create a turtle for user """
player = Player()
screen.listen()
""" a way for user for control the turtle """
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

"""
level is the score of user during the game 
when user cross the end_line score and level will be score += 1 and level += 1
and we will use level for speed up the cars and show the score of user
"""
level = 0

""" create the scoreboard and cars objects """
show_score = Scoreboard()
show_score.scoreboard(level)
car_manager = CarManager()

""" game is started... """
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    """ create a car obj in every turn """
    car_manager.car_creator()
    """ move all the cars 
        speed of the cars is depended to the score
    """
    car_manager.move_the_car(level)

    # detect when turtle cross the end line
    if player.ycor() > 260:
        level += 1
        show_score.scoreboard(level)
        player.reset_player()

    # detect when player touch one of the cars
    for car in car_manager.all_cars:
        if car.distance(player.position()) < 19:
            game_over = Scoreboard()
            game_over.game_over()
            game_is_on = False

# click to exit :))
screen.exitonclick()
