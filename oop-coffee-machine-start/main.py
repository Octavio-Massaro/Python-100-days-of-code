from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# item = MenuItem()
menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()
end = False

while not end:
    choice = input("What would you like: " + menu.get_items() + " Type 'end' to close the coffee machine\n")
    choice.lower()
    if choice == "report":
        coffee.report()
        money.report()
    elif choice == "end":
        end = True
    else:
        drink = menu.find_drink(choice)
        try:
            if coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost):
                coffee.make_coffee(drink)
        except:
            continue




