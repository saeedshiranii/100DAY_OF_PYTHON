import random
from game_data import data
from art import *


def data_printer(first, sec):
    print(logo)
    print(F'compare A is: {first["name"]}, a {first["description"]}, from {first["country"]}')
    print(vs)
    print(F'compare B is: {sec["name"]}, a {sec["description"]}, from {sec["country"]}')


first = random.choice(data)
sec = random.choice(data)

score = 0
while True:
    data_printer(first, sec)
    a = first['follower_count']
    print("a", a)
    b = sec['follower_count']
    print("b", b)
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if a > b and guess == "a":
        score += 1
        print(f"You're right! Current score: {score}")
        first = first
        sec = random.choice(data)

    elif b > a and guess == "b":
        score += 1
        print(f"You're right! Current score: {score}")
        first = sec
        sec = random.choice(data)

    elif b > a and guess == "a" or a > b and guess == "b":
        print(f"Sorry, that's wrong. Final score: {score}")
        break

