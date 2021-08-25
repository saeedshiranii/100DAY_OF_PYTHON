from turtle import Screen, Turtle


screen = Screen()
screen.bgcolor("red")
tim = Turtle()
tim.hideturtle()
tim.penup()
tim.color("white")
for i in range(20):
    tim.clear()
    answer = screen.textinput(title="user guess...", prompt="who is the murder?")
    tim.write(arg=answer, move=False, align='center', font=('Arial', 8, 'normal'))
    keep_going = screen.textinput(title="keep going", prompt="do you wanna continue?")
    if keep_going.lower() == "no":
        break


