# pypassword generator
# easy mood i want to make a password with this Arrangement : number,letter,symble


# I USE RANDOM FOR CHOOCE ELEMENTS
import random

# THIS IS THE LIST OF NUMBERS AND SYMBLES AND ALPHABET TO CRAETE PASSWORD
number = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A',
         'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
         'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbol = [')', '(', '*', '&', '^', '%', '$', '#', '@', '!', '~', '|', '/', ',', '>', '<', ')']

# NOW WE SHOULD SAY HOW MANY LETTERS AND WHATEVER WE WANT OUR PASSWORD SHOUD HAVE

num = int(input("how many number your password should have?"'\n'))
chhar = int(input("how many charactor your password should have?"'\n'))
sym = int(input("how many symble your password should have?"'\n'))

# I TAKE A EMPTY STR(d) FOR MAKE THE FINAL PASSWORD
d = ""

# NOW WE CHOOCE RANDOMLY LETTERS AND NUMBERS AND SYMBLES0
for i in range(0, num):
    a = random.choice(number)
    d = d + a

for i in range(0, chhar):
    b = random.choice(alpha)
    d = d + b

for i in range(0, sym):
    c = random.choice(symbol)
    d = d + c

print(F"YOUR FINAL PASSWORD IS {d}")
