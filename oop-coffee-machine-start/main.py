from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()
# menuItem = MenuItem()
menu = Menu()

# print(menu.get_items())
#
# moneyMachine.report()
# coffeMaker.report()
# #
# # mm = moneyMachine.process_coins()
# # print(mm)

def machine():
    """this function works as a coffee machine"""
    should_continue = True
    while should_continue:
        choice = input(f"What would you like?${menu.get_items()}")

        if choice == "off":
            print("Coffee machine turning off!!")
            should_continue = False
        elif choice == "report":
            moneyMachine.report()
            coffeMaker.report()
        else:
            drink = menu.find_drink(choice)
            if coffeMaker.is_resource_sufficient(drink):
                coffeMaker.make_coffee(drink)
                price = drink.cost
                moneyMachine.make_payment(price)
            else:
                should_continue = False



machine()