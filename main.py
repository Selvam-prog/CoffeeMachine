MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

loop_through = True
quarters = 0.25
dimes = 0.10
nickle = 0.05
pennies = 0.01
amt_mach = 0


def calculate (qcount,dcount,ncount,pcount):
    dollar = 1
    dollar = 0.25 * qcount + 0.10 * dcount + 0.05 * ncount + 0.01 * pcount
    return dollar

def is_sufficient_amount(value, user_wish):
    """Calculates the amount given by the user to buy the coffee
    and tells the user about balance amount or insufficient amount"""

    global amt_mach
    cost = MENU [user_wish]["cost"]

    if value == cost:
        amt_mach += cost
        if (is_resources_sufficient(user_wish)):
            print(f"Here is your balance amount: ${value}")
            print(f"Here is your {user_wish} . Enjoy!")
        return True
    elif value > cost:
        value = value - cost
        value = round(value,2)
        if (is_resources_sufficient(user_wish)):
            print(f"Here is your balance amount: ${value}")
            print(f"Here is your {user_wish} . Enjoy!")
            amt_mach += cost
            return True
    else:
        print(f"Sorry, your amount is less than needed.Money refunded !")
        return False

def  is_resources_sufficient(user_wish):
    global loop_through
    water = resources["water"]
    milk = resources["milk"]
    coffee= resources["coffee"]

    if user_wish == 'report':
        print(f" Water:{water}\n Milk: {milk} \n Coffee: {coffee} \n Money: {amt_mach}\n")
        return

    else:
        if water >= MENU[user_wish]["ingredients"]["water"]:
            if milk >= MENU[user_wish]["ingredients"]["milk"]:
                if coffee >= MENU[user_wish]["ingredients"]["coffee"]:
                    resources ["water"] -= MENU[user_wish]["ingredients"]["water"]
                    resources["milk"] -= MENU[user_wish]["ingredients"]["milk"]
                    resources["coffee"] -= MENU[user_wish]["ingredients"]["coffee"]
                    return True
        else:
            print("Resources are insufficient . Sorry!")
            return False









while loop_through:
    amount = 0
    user_wish = input("What would you like? (espresso/latte/cappuccino)").lower()
    if user_wish == 'off':
        loop_through = False


    elif user_wish == 'report':
        is_resources_sufficient(user_wish)
    else:
        print("Please insert coins.")
        q_count = int(input("how many quarters?:"))
        d_count = int(input("how many dimes?:"))
        n_count = int(input("how many nickles?:"))
        p_count = int(input("how many pennies?:"))
        amount = calculate(q_count,d_count,n_count,p_count)
        if (is_resources_sufficient(user_wish)):
            is_sufficient_amount(amount, user_wish)










