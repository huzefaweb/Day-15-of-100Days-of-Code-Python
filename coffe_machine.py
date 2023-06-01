# custom modules
from data import MENU, resources, profit

# Function to check if there is enough resources to make coffee..........
def is_resources_sufficient(order_ingredients):
    is_enough=True
    for item in order_ingredients:
        if order_ingredients[item]>= resources[item]:
            print(f"Sorry there is not enough {item}.")
            is_enough = False
    return is_enough


# Function to check if the money paid is equal to the cost of coffee if not refund the money and reset
def is_transaction_successful(money_recieved, drink_cost):
    if money_recieved >= drink_cost:
        change = round(money_recieved-drink_cost,2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money, Money refunded")
        return False

# Function to calculate the amount of money paid
def process_coins():
    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total_pennies = round(0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies, 2)
    return total_pennies
# if all conditions met this function would run and make the coffee
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item]-= order_ingredients[item]
    print(f"Here is your {drink_name}")

# This loop would run until the off button of machine would had not entered
# Five type of choices could be entered:
# 'off' to shut the loop
# 'report' to check the left resource
# type of coffee 'espresso' 'latte' 'cappuccino'
# then according to type the resources would be checked if enough resource is present
# ask the money check if the money is equal to cost or greater than cost return change else refund
# if everything goes ok make coffee ans Enjoy
is_on = True
while is_on:
    choice = input("what would you like? (espresso/latte/cappuccino): ").lower()
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink =MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment =process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

