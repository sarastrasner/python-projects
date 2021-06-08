from data import MENU, resources, logo


def check_resources(item):
    ingredients = MENU[item]['ingredients']
    for ingredient in ingredients:
        amount_needed = ingredients[ingredient]
        # print(f"This item requires {amount_needed} of {ingredient}")
        amount_available = resources[ingredient]
        # print(f"We have: {resources[ingredient]}")
        if amount_needed > amount_available:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def reduce_resources(item):
    ingredients = MENU[item]['ingredients']
    for ingredient in ingredients:
        amount_needed = ingredients[ingredient]
        # print(f"This item requires {amount_needed} of {ingredient}")
        amount_now_available = resources[ingredient] - amount_needed
        # print(f"There is now {amount_now_available} left of {ingredient}")
        resources[ingredient] = amount_now_available
    # print("Current ingredients: ")
    # print(resources)


def run_machine():
    print(logo)
    money = 0
    while True:
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if order == 'off':
            return None
        elif order == 'report':
            # TODO Print a report of what resources it has left (milk, coffee, etc.)
            print(f"Water: {resources['water']}ml\nMilk: "
                  f"{resources['milk']}ml\nCoffee: {resources['coffee']}\nMoney:$ {money/100}")
            continue
        elif order == "espresso":
            item_ordered = 'espresso'
        elif order == "latte":
            item_ordered = 'latte'
        elif order == "cappuccino":
            item_ordered = 'cappuccino'
        else:
            print("Please enter a valid input")
            continue

        # TODO Make sure there's enough resources when the user orders a drink
        # TODO If not enough print "Sorry, not enough water"
        if not check_resources(item_ordered):
            run_machine()

        cost_of_item_ordered = float(MENU[item_ordered]['cost']) * 100
        print(f"You ordered a {item_ordered}, which costs ${MENU[item_ordered]['cost']}0.")
        total_currency_inserted = 0
        print("Please insert coins.")
        total_currency_inserted += 25 * int(input("How many quarters?: "))
        total_currency_inserted += 10 * int(input("How many dimes?: "))
        total_currency_inserted += 5 * int(input("How many nickels?: "))
        total_currency_inserted += int(input("How many pennies?: "))
        print(f"You inserted ${total_currency_inserted/100}.")
        if total_currency_inserted < cost_of_item_ordered:
            print("Sorry that's not enough money. Money refunded.")
            run_machine()
        else:
            # TODO: Process coins and give appropriate change
            change_due = (total_currency_inserted - cost_of_item_ordered) / 100
            print(f"Here is your ${change_due} in change.\nHere is your {item_ordered} ☕️. Enjoy!")
            # TODO If transaction was successful, deduct the resources
            reduce_resources(item_ordered)
            # TODO: total money in machine
            money += cost_of_item_ordered


run_machine()


