# a tip calculator

# now we wanna get bill and percent and number of people
print("welcome to the tip calculator")
bill = float(input("what was the total bill? $ "))
percent = int(input("what percentage would you like to give? 10, 12, 15? "))
per = int(input(" How many people to split the bill? "))

""" formula = (bill/per)*1.percent"""
""" 1.percent is for paying money of food and tip (1 for food) and (0.tip  for tip) """\
calculate = ((percent/100)+1)
pay = (bill/per)*calculate
pay = round(pay, 2)
print(F"each person should pay: ${pay}")
