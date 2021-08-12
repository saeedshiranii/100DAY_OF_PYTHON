from scoreboard import Scoreboard
from middle_line import line
from paddle import Paddle
from turtle import Screen
import time
import ball


""" create a black screen """
screen = Screen()
screen.bgcolor("black")
screen.title("My Pong")
screen.setup(width=1000, height=600)
screen.tracer(0)

""" this part make sure in which level you wanna play """
difficulty = screen.textinput(title="difficulty", prompt="hard or easy")
if difficulty == "easy":
    time_sleep = 0.1
elif difficulty == "hard":
    time_sleep = 0.03
else:
    time_sleep = 0.1


""" main position of paddles"""
RIGHT_POSITION = (450, 0)
LEFT_POSITION = (-450, 0)

""" create two paddle in the main positions """
left_paddle = Paddle(LEFT_POSITION)
right_paddle = Paddle(RIGHT_POSITION)

left_scoreboard = Scoreboard()
right_scoreboard = Scoreboard()

left_scoreboard.penup()
right_scoreboard.penup()

right_scoreboard.hideturtle()
left_scoreboard.hideturtle()

left_scoreboard.color("white")
right_scoreboard.color("white")

left_scoreboard.goto(-80, 230)
right_scoreboard.goto(80, 230)


""" create two scoreboard and first scores """
left_score = 0
right_score = 0
left_scoreboard.create_scoreboard(align='left', score=left_score)
right_scoreboard.create_scoreboard(align='right', score=right_score)

""" create a line and a ball"""
ball = ball.Ball()
line()

""" these are command keys """
screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "s")
screen.onkey(left_paddle.down, "x")


""" and now battle is started :))))))))))) """
game_is_on = True
while game_is_on:
    """
    update and sleep are for make ball's speed reasonable
    """
    time.sleep(time_sleep)
    screen.update()
    ball.move()
    screen.update()

    """ if ball touch the floor or the top of screen"""
    if ball.ycor() <= -280 or ball.ycor() >= 280:
        ball.y_revers()

    """ if ball go to the end of left side of screen"""
    if ball.xcor() <= -480:
        right_score += 1
        right_scoreboard.clear()
        right_scoreboard.create_scoreboard(align='right', score=right_score)
        ball.goto(0, 0)
        screen.update()

    """if ball go to the end of left side of screen"""
    if ball.xcor() >= 480:
        left_score += 1
        left_scoreboard.clear()
        left_scoreboard.create_scoreboard(align='left', score=left_score)
        ball.goto(0, 0)
        screen.update()

    """ if ball touch the right paddle """
    if right_paddle.distance(ball) < 40 and ball.xcor() > 430:
        ball.x_revers()
        ball.backward(41)

    """ if ball touch the left paddle """
    if left_paddle.distance(ball) < 40 and ball.xcor() > -460:
        ball.x_revers()
        ball.forward(41)


screen.exitonclick()
