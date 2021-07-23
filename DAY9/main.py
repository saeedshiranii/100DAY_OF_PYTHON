# A PROJECT FOR COUNT BIDERS AND HOW MUCH THEY ARE BIDING


import os

biders = {}
while True:
    keep = input(" there is any body for biding ? (y/n) : ").lower()

    if keep == "y":

        name = input("what is your name ?").lower()
        bid = int(input("how much you biding ? $"))
        biders[name] = bid
        os.system('cls')

    elif keep == "n":
        os.system('cls')
        break

    else:
        print("erorr : pls choose corecctly ")
        continue

print(biders)

total = 0
for i in biders:

    if biders[i] > total:
        total = biders[i]
        person = i

print(f"the winner of this biding is {person} with {total}$")


