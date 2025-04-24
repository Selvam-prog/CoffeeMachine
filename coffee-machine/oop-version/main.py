from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()
loop_through = True

while loop_through:

    user_input= input(f"What would you like to have ?{menu.get_items()} ").lower()





    ### "To give the machine for service , when the user input is off"###
    if user_input == "off":
        loop_through = False

    ### "To print the report of the present resources in the coffee maker" ###
    elif user_input == "report":
        coffee_maker.report()
        money_machine.report()
    else:
    ### "Check if the user input is available in the items list and check for available resources in the machine and
     #check if the money is sufficient money and then give them the requested variety of coffee"###
        drink = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink):
            print(f"The money for ur favourite drink is : {drink.cost}")
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)










