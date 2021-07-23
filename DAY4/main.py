import random

# a program for rock paper scissor

# first create list to choose operation
list_of_positions = ["rock", "paper", "scissor"]

# now we gonna choose a random position for system
system = random.choice(list_of_positions)
print("s", system)

# and now we let user choose what he/she want to choose
# we should create a while loop to be sure users input is correct
while 2 < 3:
    user = input("rock, paper, scissor ??  ").lower()
    if user == "rock" or user == "paper" or user == "scissor":
        break
    else:
        print(" please enter correctly.")


# now we understand who is winner? system or user?
if user == "rock":
    if system == "rock":
        print("equal")
    elif system == "paper":
        print(F"you lose.system was {system} and you have {user}")
    else:
        print(F"you win.system was {system} and you have {user} ")

elif user == "paper":
    if system == "rock":
        print(F"you win.system was {system} and you have {user} ")
    elif system == "paper":
        print("equal")
    else:
        print(F"you lose.system was {system} and you have {user}")

else:
    if system == "rock":
        print(F"you lose.system was {system} and you have {user}")
    elif system == "paper":
        print(F"you win.system was {system} and you have {user} ")
    else:
        print("equal")
