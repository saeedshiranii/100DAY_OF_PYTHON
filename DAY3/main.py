# a program for playing fizzbuzz

number = int(input('what is the last number in your game? '))

a = 1

while (a <= number):

    if a % 3 == 0 and a % 5 != 0:
        print("fizz")
    elif a % 5 == 0 and a % 3 != 0:
        print("buzz")
    elif a % 3 == 0 and a % 5 == 0:
        print("fizzbuzz")
    else:
        print(a)

    a += 1