from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


""" a object for getting order and show what device has"""
item = Menu()

""" object for check resources enough or not and report them to the user"""
coffee_maker = CoffeeMaker()

""" an object for getting payment and give report the amount of money """
money = MoneyMachine()

is_on = True
while is_on:
    select = item.get_items()
    order = input(F"What would you like? ({select}):")
    if order == "off":
        is_on = False
    elif order == "report":
        coffee_maker.report()
        money.report()
    else:
        drink = item.find_drink(order)
        check = coffee_maker.is_resource_sufficient(drink)
        if check == False:
            print("Sorry there is not enough water.")
        else:
            pay = float(money.make_payment(drink.cost))
            coffee_maker.make_coffee(drink)



