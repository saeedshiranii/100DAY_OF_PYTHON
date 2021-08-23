from turtle import Turtle, Screen
import turtle as t

screen = Screen()
screen.title("U.S  STATES GAME")
img = "blank_states_img.gif"
screen.addshape(img)
t.shape(img)


answer = screen.textinput(title="Guess the state", prompt="What's another state's name?")

screen.exitonclick()
