from turtle import Screen, Turtle
from paddle import Paddle
from random import randint
import ball
import time


RIGHT_POSITION = (450, 0)
LEFT_POSITION = (-450, 0)

screen = Screen()
screen.bgcolor("black")
screen.title("My Pong")
screen.setup(width=1000, height=600)
screen.tracer(0)

left_paddle = Paddle(LEFT_POSITION)
right_paddle = Paddle(RIGHT_POSITION)
ball = ball.Ball()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "x")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    screen.update()

    if ball.ycor() <= -280 or ball.ycor() >= 280:
        ball.revers()

    if ball.xcor() <= -480 or ball.xcor() >= 480:
        ball.goto(0, 0)
        screen.update()
        ball.goto(0, 0)



screen.exitonclick()
