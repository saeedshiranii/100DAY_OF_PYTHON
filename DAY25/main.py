from turtle import Turtle, Screen
import turtle as t
import pandas
import pandas as pd


def get_user_guess(counter):
    """
    create a function for get users guess's with a popup windows
    :param counter:
    :return:
    """
    answer = screen.textinput(title=F"{counter}/50 Guess the state", prompt="What's another state's name?")
    answer = answer.title()
    return answer


""" create a screen and and load an image in it """
screen = Screen()
screen.title("U.S  STATES GAME")
img = "blank_states_img.gif"
screen.addshape(img)
t.shape(img)


""" open the source file of states. """
data = pd.read_csv('50_states.csv')
states_list = data.state.to_list()


""" get user's guess """
states_guessed = []
user_answer = get_user_guess(len(states_guessed))


while len(states_guessed) < 50:
    if user_answer == 'Exit':
        break

    if user_answer in states_guessed:
        user_answer = get_user_guess(len(states_guessed))

    if user_answer in states_list:  # user guess is right
        states_guessed.append(user_answer)
        timmy = Turtle()
        timmy.hideturtle()
        timmy.penup()
        state_data = data[data.state == user_answer]
        x = int(state_data.x)
        y = int(state_data.y)
        timmy.goto(x, y)
        timmy.write(arg=user_answer, move=False, align="center", font=('Arial', 8, 'normal'))
        user_answer = get_user_guess(len(states_guessed))

    else:  # user guess is not right or have typo
        user_answer = get_user_guess(len(states_guessed))


""" a file for user to see which states are missed during the game """
missing_states = []
for state in states_list:
    if state not in states_guessed:
        missing_states.append(state)

states_missed = pandas.DataFrame(missing_states)
states_missed.to_csv("states_you_missed.csv")
