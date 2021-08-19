from car_manager import CarManager
from scoreboard import Scoreboard
from turtle import Screen, Turtle
from player import Player
from line import line
import time

FINISH_LINE_Y = 300


screen = Screen()
screen.bgcolor("black")
screen.setup(width=700, height=600)
screen.tracer(0)
line()


player = Player()
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

level = 0
show_score = Scoreboard()
game_over = Scoreboard()
show_score.scoreboard(level)
car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.car_creator()
    car_manager.move_the_car(level)

    if player.ycor() > 260:
        level += 1
        show_score.scoreboard(level)
        player.reset_player()

    for car in car_manager.all_cars:
        if car.distance(player.position()) < 19:
            game_over = Scoreboard()
            game_over.game_over()
            game_is_on = False

screen.exitonclick()
