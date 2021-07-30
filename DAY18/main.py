import random
import turtle as t
from turtle import Turtle, Screen


color_list = [(231, 206, 83), (229, 147, 85), (119, 166, 186), (160, 13, 19), (30, 110, 159), (235, 81, 44)
              ,(5, 99, 37), (176, 19, 14), (187, 187, 25), (121, 177, 144), (207, 62, 22), (23, 132, 41), (245, 201, 4),
              (10, 42, 77), (13, 64, 41), (137, 83, 98), (83, 17, 24), (46, 168, 74), (3, 66, 140), (173, 133, 149),
              (36, 25, 21), (45, 151, 198), (220, 63, 68), (227, 171, 162), (73, 135, 188), (172, 204, 174)]

tim = t.Turtle()
screen = Screen()
t.colormode(255)

tim.penup()
tim.hideturtle()
tim.goto(-200, -250)
tim.speed("fastest")
number_of_dot = 100

for dot_counter in range(1, number_of_dot+1):
    random_color = random.choice(color_list)
    tim.dot(20, random_color)
    tim.forward(50)

    if dot_counter % 10 == 0:
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(500)
        tim.left(180)

screen.exitonclick()
