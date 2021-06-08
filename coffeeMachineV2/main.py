from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def run_machine():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    while True:
        # TODO: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
        order = input(f"What would you like? ({menu.get_items()}): ")
        # TODO: Turn off the Coffee Machine by entering “off” to the prompt.
        if order == 'off':
            break
        # TODO: Print report
        elif order == 'report':
            coffee_maker.report()
            money_machine.report()
        else:
            validated_order = menu.find_drink(order)
            # TODO: Check resources sufficient
            if coffee_maker.is_resource_sufficient(validated_order):
                # TODO: Process Coins
                # TODO: Check transaction successful
                money_machine.make_payment(validated_order.cost)
                coffee_maker.make_coffee(validated_order)


run_machine()

