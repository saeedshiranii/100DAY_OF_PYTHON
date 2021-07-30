from menu import MENU
from menu import resources


def check_resources(list_of_resources, user_order):
    see_resources = MENU[user_order]["ingredients"]

    for key in see_resources:
        if see_resources[key] > list_of_resources[key]:
            print(F"Sorry there is not enough {key}.")
            return False
    return True


def get_money():
    print("insert coins.")
    total = int(input("how many penny do you have? ")) * 0.01
    total += int(input("how many dime do you have? ")) * 0.1
    total += int(input("how many nickle do you have? ")) * 0.05
    total += int(input("how many quarter do you have? ")) * 0.25

    return total


def change_resources(resource, user_order):
    for key in MENU[user_order]["ingredients"]:
        main = resource[key]
        usage = MENU[user_order]["ingredients"][key]
        remain = main - usage
        resource[key] = remain


def give_me_coffee():
    while True:
        order = input("What would you like? (espresso/latte/cappuccino): ")
        if order == "report":
            print(F'water: {resources["water"]} \n milk: {resources["milk"]}\n coffee: {resources["coffee"]}\n ')

        elif order == "off":
            print("have a good day.")
            break

        else:
            if check_resources(resources, order) == False:
                break
            money = get_money()
            cost = MENU[order]["cost"]
            if money < cost:
                print("you have not enough money.")
            else:
                print(F" here is your coffee ☕ and this is your change {round(money - cost, 2)}$.enjoy:))) ")
                change_resources(resources, order)


give_me_coffee()


