from sound import crash_sound, eating_sound
from wall_printer import wall_printer
from scoreboard import Scoreboard
from turtle import Screen
from random import choice
from snake import Snake
from food import Food
from time import sleep


List_color = ["blue", "red", "yellow", "purple", "green"]
random_color = choice(List_color)  # this color will be used for food and wall

# create a black screen
screen = Screen()
scoreboard = Scoreboard()
game_over = Scoreboard()
screen.bgcolor("black")
screen.setup(width=820, height=620)
screen.title("my snake")
wall_printer(random_color)
screen.tracer(0)

snake = Snake()
food = Food()
food.refresh(random_color)


# control our snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# Now game is on
game_is_on = True
while game_is_on:

    screen.update()
    sleep(0.07)
    scoreboard.update_scoreboard()
    snake.move()

    # Detect touch the food
    if snake.head.distance(food) < 15:
        eating_sound()
        snake.increase_length()
        scoreboard.increase_score()
        random_color = choice(List_color)
        wall_printer(random_color)
        food.refresh(random_color)

    # Detect touch the wall
    if snake.head.xcor() < -390 or snake.head.xcor() > 390 or snake.head.ycor() < -290 or snake.head.ycor() > 265:
        crash_sound()
        print("Game is over.")
        game_is_on = False
        game_over.game_over()
        answer = screen.textinput(title="menu", prompt="do you wanna play again? (yes/no)")
        if answer == "yes":
            game_over.clear_data()
            scoreboard.clear_data()
            scoreboard = Scoreboard()
            scoreboard.update_scoreboard()
            snake.recycle_snake()
            screen.listen()
            game_is_on = True
            print("Game is restarted.")
        else:
            screen.bye()

    # Detect snake touch his body
    for part in snake.snake_body[1:]:

        if snake.head.distance(part) < 1:
            crash_sound()
            game_is_on = False
            game_over.game_over()
            answer = screen.textinput(title="menu", prompt="do you wanna play again? (yes/no)")
            if answer == "yes":
                game_over.clear_data()
                scoreboard.clear_data()
                scoreboard = Scoreboard()
                scoreboard.update_scoreboard()
                snake.recycle_snake()
                screen.listen()
                game_is_on = True
                print("Game is restarted.")
            else:
                screen.bye()

screen.exitonclick()

