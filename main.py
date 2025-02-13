from logo import coffee_logo
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
print(coffee_logo)

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

system_continue = True


while system_continue:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()

    if choice == "off":
        print("Coffee Machine is shutting down.")
        system_continue = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
